# Comprehensive University Catalog Data

DEPARTMENTS = [
    {
        "code": "CSE",
        "name": "Department of Computer Science & Engineering",
        "hod": "Dr. Eleanor Vance",
        "established_year": 1995,
        "laboratories": ["Advanced Computing Lab", "AI & Deep Learning Lab", "Cloud Infrastructure Center", "Networks Security Lab", "IoT Prototyping Lab"],
        "programs": ["B.Tech Computer Science", "M.Tech Software Engineering", "Ph.D Computing"]
    },
    {
        "code": "ECE",
        "name": "Department of Electronics & Communication",
        "hod": "Dr. Rajeshwar Rao",
        "established_year": 1998,
        "laboratories": ["VLSI Design Center", "Embedded Systems Lab", "Digital Signal Processing Lab", "RF & Microwave Lab", "Robotics Lab"],
        "programs": ["B.Tech Electronics & Comm", "M.Tech VLSI", "Ph.D Electronics"]
    },
    {
        "code": "IT",
        "name": "Department of Information Technology",
        "hod": "Dr. Meenakshi Sundaram",
        "established_year": 2002,
        "laboratories": ["Web Technologies Lab", "Database Engineering Lab", "Big Data Analytics Lab", "Cybersecurity Sandbox"],
        "programs": ["B.Tech Information Technology", "M.Tech Data Science"]
    },
    {
        "code": "MECH",
        "name": "Department of Mechanical Engineering",
        "hod": "Dr. Vikramaditya Sen",
        "established_year": 1992,
        "laboratories": ["CAD/CAM Lab", "Thermodynamics Lab", "Fluid Mechanics Lab", "Automotive Research Center", "Mechatronics Lab"],
        "programs": ["B.Tech Mechanical Engineering", "M.Tech Thermal Eng"]
    },
    {
        "code": "CIVIL",
        "name": "Department of Civil & Structural Engineering",
        "hod": "Dr. Sunita Patel",
        "established_year": 1990,
        "laboratories": ["Structural Engineering Lab", "Soil Mechanics Lab", "Surveying & GIS Lab", "Environmental Engineering Lab"],
        "programs": ["B.Tech Civil Engineering", "M.Tech Structural Eng"]
    },
    {
        "code": "MGMT",
        "name": "School of Management Studies",
        "hod": "Dr. Jonathan Hayes",
        "established_year": 2005,
        "laboratories": ["Financial Analytics Terminal", "Business Simulation Lab", "Executive Strategy Suite"],
        "programs": ["MBA Financial Management", "MBA Marketing & Operations", "Executive MBA"]
    }
]

COURSE_CATALOG = [
    {
        "code": "CS101",
        "name": "Introduction to Computer Science & Problem Solving",
        "department": "Computer Science",
        "semester": 1,
        "credits": 4,
        "syllabus": "Problem solving techniques, Flowcharts, Pseudocode, Python syntax, Data structures, File I/O, Exception handling, Recursion.",
        "modules": [
            {"num": 1, "title": "Algorithmic Thinking & Flowcharts", "desc": "Decomposition of problems, stepwise refinement, flow control."},
            {"num": 2, "title": "Python Control Structures", "desc": "Conditionals, iterative loops, comprehension constructs."},
            {"num": 3, "title": "Functions & Modular Architecture", "desc": "Parameters, scoping, lambda functions, standard libraries."},
            {"num": 4, "title": "Data Structures & Collections", "desc": "Lists, tuples, dictionaries, sets, hashing mechanics."},
            {"num": 5, "title": "File Handling & Persistence", "desc": "Text files, binary serialization, error handling mechanisms."}
        ]
    },
    {
        "code": "CS201",
        "name": "Object Oriented Software Engineering",
        "department": "Computer Science",
        "semester": 2,
        "credits": 4,
        "syllabus": "OOP paradigms, Encapsulation, Inheritance, Polymorphism, Design patterns, UML Modeling, SOLID principles, JUnit testing.",
        "modules": [
            {"num": 1, "title": "Object-Oriented Fundamentals", "desc": "Classes, constructors, lifecycle management, memory heap vs stack."},
            {"num": 2, "title": "Inheritance & Abstract Interfaces", "desc": "Dynamic dispatch, polymorphism, method overriding vs overloading."},
            {"num": 3, "title": "SOLID Design Principles", "desc": "Single responsibility, open-closed, Liskov substitution, dependency injection."},
            {"num": 4, "title": "GoF Creational & Structural Design Patterns", "desc": "Factory, Singleton, Adapter, Decorator, Facade patterns."},
            {"num": 5, "title": "Behavioral Patterns & Unit Testing", "desc": "Observer, Strategy, State pattern, TDD with JUnit / PyTest."}
        ]
    },
    {
        "code": "CS301",
        "name": "Data Structures and Algorithm Design",
        "department": "Computer Science",
        "semester": 3,
        "credits": 4,
        "syllabus": "Asymptotic analysis, Stacks, Queues, Linked lists, Trees, AVL, Red-Black trees, Graphs, BFS/DFS, Greedy methods, Dynamic programming.",
        "modules": [
            {"num": 1, "title": "Complexity Analysis & Elementary Structures", "desc": "Big-O, Omega, Theta notation, Amortized analysis, Stacks & Queues."},
            {"num": 2, "title": "Non-Linear Structures: Trees & Heaps", "desc": "Binary search trees, AVL rotations, Min/Max binary heaps, Priority queues."},
            {"num": 3, "title": "Graph Algorithms & Traversals", "desc": "Adjacency representations, BFS, DFS, Topological sort, Dijkstra, Prim, Kruskal."},
            {"num": 4, "title": "Divide & Conquer and Greedy Paradigms", "desc": "Merge sort, Quick sort, Fractional knapsack, Huffman encoding."},
            {"num": 5, "title": "Dynamic Programming & NP-Completeness", "desc": "0/1 Knapsack, LCS, Floyd-Warshall, P vs NP, Reduction techniques."}
        ]
    },
    {
        "code": "CS401",
        "name": "Database Management Systems & SQL Analytics",
        "department": "Computer Science",
        "semester": 4,
        "credits": 4,
        "syllabus": "Relational algebra, ER diagrams, Normalization (1NF to BCNF), Transaction management, ACID properties, Indexing, B+ Trees, NoSQL.",
        "modules": [
            {"num": 1, "title": "Relational Data Modeling & ER Diagrams", "desc": "Entity sets, cardinalities, relational schemas, foreign key constraints."},
            {"num": 2, "title": "Advanced SQL & Relational Algebra", "desc": "Subqueries, window functions, CTEs, joins, query optimizer plans."},
            {"num": 3, "title": "Schema Normalization & Functional Dependencies", "desc": "Armstrong axioms, 1NF, 2NF, 3NF, Boyce-Codd Normal Form decomposition."},
            {"num": 4, "title": "Transactions & Concurrency Control", "desc": "ACID properties, serializability, two-phase locking (2PL), deadlock resolution."},
            {"num": 5, "title": "Storage, Indexing & NoSQL Paradigms", "desc": "B+ Trees, hashing indexes, document databases, key-value stores."}
        ]
    },
    {
        "code": "CS501",
        "name": "Operating Systems & Concurrency",
        "department": "Computer Science",
        "semester": 5,
        "credits": 3,
        "syllabus": "Process lifecycle, IPC, Threading, CPU scheduling, Synchronization, Semaphores, Deadlocks, Virtual memory, Page replacement, File systems.",
        "modules": [
            {"num": 1, "title": "Processes, Threads & Dual-Mode Execution", "desc": "Context switching, PCB, kernel vs user space, system calls."},
            {"num": 2, "title": "CPU Scheduling Algorithms", "desc": "FCFS, SJF, Round Robin, Multilevel Feedback Queues."},
            {"num": 3, "title": "Synchronization & Critical Section Problem", "desc": "Peterson algorithm, mutex locks, semaphores, monitors, classic IPC problems."},
            {"num": 4, "title": "Memory Management & Virtual Memory", "desc": "Paging, segmentation, TLB, demand paging, FIFO, LRU page replacement."},
            {"num": 5, "title": "Storage, I/O & File System Architecture", "desc": "Inodes, directory structures, disk scheduling algorithms (SSTF, SCAN, LOOK)."}
        ]
    },
    {
        "code": "AI601",
        "name": "Machine Learning & Deep Neural Networks",
        "department": "Computer Science",
        "semester": 6,
        "credits": 4,
        "syllabus": "Supervised learning, Linear regression, Logistic classification, SVMs, Decision trees, Ensembles, Backpropagation, CNNs, Transformers.",
        "modules": [
            {"num": 1, "title": "Statistical Foundations & Linear Models", "desc": "Cost functions, gradient descent, regularized regression (L1/L2)."},
            {"num": 2, "title": "Classification, SVMs & Kernel Tricks", "desc": "Maximum margin classifiers, non-linear kernels, ROC/AUC metrics."},
            {"num": 3, "title": "Ensemble Methods & Tree Algorithms", "desc": "Random forests, gradient boosting (XGBoost, LightGBM), stacking."},
            {"num": 4, "title": "Deep Feedforward Networks & Backprop", "desc": "Activation functions, cross-entropy loss, Adam optimization, regularization."},
            {"num": 5, "title": "Computer Vision & Transformer Architectures", "desc": "Convolutions, ResNet, Self-attention, BERT, GPT foundation models."}
        ]
    }
]
