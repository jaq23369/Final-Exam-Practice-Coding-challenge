// Exercise 4 — Longest Valid Parentheses
// Given a string containing only '(' and ')', return the length of the
// longest well-formed parentheses substring.

import assert from "node:assert";

function longestValidParentheses(s: string): number {
  const stack: number[] = [-1];
  let longest = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
      continue;
    }

    stack.pop();

    if (stack.length === 0) {
      stack.push(i);
    } else {
      longest = Math.max(longest, i - stack[stack.length - 1]);
    }
  }

  return longest;
}

// Approach:
// Keep a stack of indices. The bottom value stores the index before the
// current valid search window. For each ')', pop one possible matching '('.
// If the stack becomes empty, the current ')' is the new invalid boundary.
// Otherwise, the distance from the current index to the stack top is the
// length of the current valid substring.
//
// Time:  O(n) — each character index is pushed and popped at most once.
// Space: O(n) — the stack can store up to n indices.

assert.strictEqual(longestValidParentheses("(()"), 2);
assert.strictEqual(longestValidParentheses(")()())"), 4);
assert.strictEqual(longestValidParentheses(""), 0);
assert.strictEqual(longestValidParentheses("()(()"), 2);
assert.strictEqual(longestValidParentheses("(()())"), 6);

console.log("All tests passed!");

export { longestValidParentheses };
