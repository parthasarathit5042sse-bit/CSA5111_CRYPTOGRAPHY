CNS LIST OF PROGRAMS — C PROGRAM FILES
========================================

This ZIP contains 40 separate .c files, numbered to match the uploaded PDF's list of 40 questions.
Open the folder in VS Code / GitHub Codespaces. Compile a file with:
    gcc 01_caesar_cipher.c -o program
Run it with:
    ./program

For a different file, replace the filename. In Windows GCC terminal, run the output executable as:
    .\program.exe

IMPORTANT HONEST NOTES
----------------------
- These are educational examples mapped to the wording of the supplied practical list.
- Some PDF questions ask for explanations, attack analysis, or full industrial cryptographic algorithms. Those are represented by focused demonstrations/explanations rather than falsely claiming a complete secure implementation.
- In particular, files for DES key scheduling, SHA-3 lane counting, CBC/CTR mode examples, CMAC, and several security-analysis questions are teaching demonstrations, not production cryptography.
- Playfair, Caesar, affine, Vigenere, substitution, RSA small-number key calculation, and Diffie-Hellman examples are executable implementations/demonstrations.
- The PDF's Hill key is visually split as 94 / 57; file 12 interprets it as [[9,4],[5,7]]. Confirm this interpretation with your instructor if the layout was intended differently.
- Never use these classical ciphers or toy examples to protect real passwords, wallet keys, or sensitive data.
