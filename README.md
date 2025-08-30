# Programming Language Transcoder  

## 📌 Project Overview  
The **Programming Language Transcoder** is a tool designed to automatically translate source code from one programming language to another while preserving its logic, structure, and functionality.  
It leverages parsing techniques and intermediate representations to achieve accurate translations, reducing the effort required for code migration, legacy system modernization, and cross-platform development.  

This project was developed as part of **Mini Project 1-a (REV-2019 ‘C’ Scheme)** in the **Third Year (TE Sem-V), Electronics & Computer Science Engineering**, at **SIES Graduate School of Technology, Nerul (Mumbai University)**.  

---

## 🚀 Features  
- Automatic translation of code between programming languages.  
- Maintains readability and functional equivalence of source code.  
- Supports COBOL ➝ Python conversion (demo implementation).  
- Error detection for invalid or incomplete syntax.  
- Extensible design to add support for additional languages.  

---

## 🛠️ Tech Stack  
- **Languages:** Python (Core implementation)  
- **Concepts Used:**  
  - Parsing techniques  
  - Intermediate representations  
  - Rule-based and ML-assisted translation  
- **Tools:**  
  - Python standard libraries  
  - File I/O for code handling  

---

## 📂 Project Structure  
```
├── data/                # Sample input COBOL files  
├── output/              # Translated Python code  
├── tests/               # Test cases for validation  
├── transcoder.py        # Core transcoder implementation  
├── README.md            # Project documentation  
└── report/              # Project report & references  
```

---

## 🧪 Test Cases  
Example COBOL-to-Python translations:  

| COBOL Input | Expected Python Output |
|-------------|-------------------------|
| `ADD 1 TO total GIVING total.` | `total += 1` |
| `IF total > 100 THEN DISPLAY 'Total is greater than 100'. END-IF.` | `if total > 100:\n    print("Total is greater than 100")` |
| `PERFORM VARYING i FROM 1 BY 1 UNTIL i > 5 DISPLAY i END-PERFORM.` | `for i in range(1, 6):\n    print(i)` |

✔️ More detailed test cases are included in the `/tests` folder.  

---

## 📈 Future Scope  
- Multi-language support (Java, C++, Python, etc.).  
- AI/ML integration for context-aware translation.  
- IDE/plugin integration for real-time translation.  
- Modernization of large COBOL/Fortran legacy codebases.  

---

## 👩‍💻 Contributor  
- **Tanishka Deshpande**  
This project is for **educational purposes** under the University of Mumbai curriculum.  
You may use or extend it for academic or research purposes.  
