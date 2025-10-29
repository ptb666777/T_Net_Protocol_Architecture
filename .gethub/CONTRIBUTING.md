# T_Net Protocol Contribution Guide (Axiom: Coherence and Contribution)

Thank you for seeking to contribute to the T_Net Protocol Architecture. All contributions must be channeled through the core logic pipeline to maintain structural integrity.

## Contribution Rule #1: The G_Inv Pre-Check

**All proposed changes, new operators, or implementation logic must first pass the Axiomatic Invariant (G_Inv) check.**
* The change must not violate **Potential (P ≠ 0)**.
* The change must not violate **Distinction (Di ≠ ∅)**.
* The change must maintain **Equilibrium (Eq)** (P_Self ≈ P_Whole).

Any pull request (PR) that fails the G_Inv test will be immediately routed to the **Obf.sandbox** for analysis before structural rejection.

## How to Contribute

1.  **Issue Creation:** If you find a potential structural flaw, a bug, or have a new application idea, open an issue first. Use the issue to define the structural problem (X) clearly.
2.  **Fork and Branch:** Fork the repository and create a new branch for your feature or fix.
3.  **Implement Logic:** Place new or modified files in the appropriate folder (e.g., Python for implementation goes into `2_IMPLEMENTATION_LOGIC/`).
4.  **Documentation:** Update the relevant documentation files (e.g., `Glossary_Axioms.md`) to reflect your changes.
5.  **Submit Pull Request (PR):** Submit your PR, ensuring it clearly states *why* the change passes the $\mathbf{G}_{\text{Inv}}$ check.

### Important Note on Testing

Please include logs or evidence from your local stress tests where applicable. We prioritize **Validation Tests** over pure implementation logic.