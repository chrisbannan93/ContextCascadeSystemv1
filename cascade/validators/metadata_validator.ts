// validators/metadata_validator.ts
// -------------------------------------------------
// ContextCascade Metadata Validator
// -------------------------------------------------
// Responsibilities:
//   • Parse top-of-file `@meta` JSON blocks
//   • Verify required fields per fileType / subtype
//   • Enforce editPolicy + routeScope value constraints
//   • Provide a structured API for loop controller
//
// Usage (inside loop controller):
//   import { validateFile } from "./validators/metadata_validator";
//   const report = validateFile(filePath, rawContent);
//   if (!report.valid) throw new Error(report.message);
// -------------------------------------------------

import fs from "fs";

// -------------------- Types ----------------------

interface MetaBlock {
  fileType: string;
  purpose?: string;
  editPolicy: "appendOnly" | "appendOrReplace" | "incrementOnly" | "readonly" | "replaceOnly";
  routeScope?: string;
  [key: string]: unknown;
}

interface ValidationReport {
  valid: boolean;
  message: string;
  warnings: string[];
  meta?: MetaBlock;
}

// -------------------- Constants ------------------

const REQUIRED_FIELDS = ["fileType", "editPolicy"] as const;
const ALLOWED_FILE_TYPES = new Set([
  "permanent",
  "immutable",
  "rolling",
  "append-only",
  "temporary",
  "counter",
  "evictable",
  "protected",
  "structural"
]);

const ALLOWED_EDIT_POLICIES = new Set([
  "appendOnly",
  "appendOrReplace",
  "incrementOnly",
  "readonly",
  "replaceOnly",
]);

// -------------------- Helper Functions -----------

function extractMeta(raw: string): { meta?: MetaBlock; remainder: string } {
  const match = raw.match(/<!--\s*@meta\s*({[\s\S]*?})\s*-->/m);
  if (!match) return { remainder: raw };
  try {
    const meta = JSON.parse(match[1]);
    return { meta, remainder: raw.replace(match[0], "") };
  } catch (e) {
    throw new Error("Invalid JSON in @meta block: " + e.message);
  }
}

function validateMeta(meta: MetaBlock, filePath: string): ValidationReport {
  const warnings: string[] = [];

  // Required fields
  for (const key of REQUIRED_FIELDS) {
    if (!(key in meta)) {
      return {
        valid: false,
        message: `Missing required field \"${key}\" in @meta for ${filePath}`,
        warnings,
      };
    }
  }

  // fileType check
  if (!ALLOWED_FILE_TYPES.has(meta.fileType)) {
    return {
      valid: false,
      message: `Invalid fileType \"${meta.fileType}\" in ${filePath}`,
      warnings,
    };
  }

  // editPolicy check
  if (!ALLOWED_EDIT_POLICIES.has(meta.editPolicy)) {
    return {
      valid: false,
      message: `Invalid editPolicy \"${meta.editPolicy}\" in ${filePath}`,
      warnings,
    };
  }

  // routeScope recommendation
  if (!meta.routeScope) {
    warnings.push("routeScope missing — recommend specifying domain or global.");
  }

  return { valid: true, message: "OK", warnings, meta };
}

// -------------------- Public API -----------------

export function validateFile(filePath: string, raw?: string): ValidationReport {
  const content = raw ?? fs.readFileSync(filePath, "utf8");
  const { meta } = extractMeta(content);
  if (!meta) {
    return {
      valid: false,
      message: `No @meta block found in ${filePath}`,
      warnings: [],
    };
  }
  return validateMeta(meta, filePath);
}

// CLI utility (optional)
if (require.main === module) {
  const target = process.argv[2];
  if (!target) {
    console.error("Usage: ts-node metadata_validator.ts <filePath>");
    process.exit(1);
  }
  const report = validateFile(target);
  if (report.valid) {
    console.log("✔", target, "validated");
    if (report.warnings.length) console.warn("Warnings:", report.warnings.join("; "));
  } else {
    console.error("✖", target, report.message);
    process.exit(2);
  }
}
