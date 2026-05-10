## Exercise 4 (TypeScript) — Write the Algorithm

Given a string `s` containing only `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

**Input:** `s: string`  
**Output:** `number`

**Constraints:** O(n) time required. Include a brief justification of your approach and its complexity.

**Tests (using Node.js `assert`):**
```typescript
import assert from "node:assert";

assert.strictEqual(longestValidParentheses("(()"), 2);
assert.strictEqual(longestValidParentheses(")()())"), 4);
assert.strictEqual(longestValidParentheses(""), 0);
assert.strictEqual(longestValidParentheses("()(()"), 2);
assert.strictEqual(longestValidParentheses("(()())"), 6);
```