# Code-review workflow scenarios

Use these synthetic scenarios to evaluate the instructions in the git code-review sub-skill and its publication reference. Simulate the user choices and GitHub responses without submitting reviews or changing code. Check the complete output and hand-offs, not just whether the instructions contain particular phrases.

| Scenario | Input and expected behavior |
|---|---|
| Minor issues | A complete PR review finds one Low, Optional naming issue. Recommend Approve and list the issue with its location and full comment. |
| Required issue | A High, Required spec mismatch and Low, Optional smell are on changed lines. Recommend Request changes; list the mismatch first and label both comments. |
| Selection | The user selects comments 1 and 3 of three and Request changes. Prepare one review with those two comments; all findings still inform the recommendation. |
| Generated body | The user chooses Approve and supplies no overall comment. Generate the template body and submit without asking for separate approval. |
| Existing issue | An outdated resolved thread raises the same concern in different words. Verify its current status, suppress the duplicate suggestion, link the thread and consider outstanding work in the verdict. |
| Previous findings | An earlier non-minor finding remains unfixed or cannot be verified. Show evidence and ask explicitly whether to continue the review. |
| Updated PR | The PR head changes after selection. Refresh the scope, rerun affected reviews, show updated suggestions and request new selections before submission. |
| Repository | Review a repository path with no diff. Capture the revision and paths, assess existing code including applicable UI/UX, and report findings without making changes. |
| Development | Review committed and pending changes with an intended untracked file. Capture and fingerprint the pending scope, review it and report without making changes. |
| Incomplete coverage | Security analysis fails or a known spec is inaccessible. Report the limitation; do not present incomplete essential coverage as clean or recommend unsupported approval. |
| Security uncertainty | An issue needs verification. Report the evidence gap and offer an investigation ticket; create it only if the user selects it. |
| Publication failure | GitHub rejects the selected review. Report failure, preserve the proposed review and avoid silently changing the outcome. |

On 2026-10-29, an independent reviewer simulated all 12 scenarios against the instructions; all passed as instruction-driven simulations. This did not exercise a live PR, GitHub API, browser or actual agent execution.
