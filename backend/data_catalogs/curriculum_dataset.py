"""
Collexa Data Catalog Module: curriculum_dataset.py
Description: Full engineering and sciences course curriculum maps with credit allocations
"""
from typing import Dict, List, Any

CATALOG_METADATA = {
    'catalog_name': 'curriculum_dataset',
    'description': 'Full engineering and sciences course curriculum maps with credit allocations',
    'version': '2.5.0',
    'last_updated': '2026-08-29'
}

CATALOG_DATA: List[Dict[str, Any]] = [
    {
        'id': 1,
        'code': 'CAT-ITEM-0001',
        'title': 'Academic Standard Curriculum Item #1',
        'department': 'Electronics & Comm',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 1',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.1: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.1: Architectural Implementation and Data Structures',
            'Topic 3.1: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.1: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 2',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 2,
        'code': 'CAT-ITEM-0002',
        'title': 'Academic Standard Curriculum Item #2',
        'department': 'Information Tech',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 2',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.2: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.2: Architectural Implementation and Data Structures',
            'Topic 3.2: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.2: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 3',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 3,
        'code': 'CAT-ITEM-0003',
        'title': 'Academic Standard Curriculum Item #3',
        'department': 'Mechanical Eng',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 3',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.3: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.3: Architectural Implementation and Data Structures',
            'Topic 3.3: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.3: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 4',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 4,
        'code': 'CAT-ITEM-0004',
        'title': 'Academic Standard Curriculum Item #4',
        'department': 'Civil Eng',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 4',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.4: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.4: Architectural Implementation and Data Structures',
            'Topic 3.4: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.4: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 5',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 5,
        'code': 'CAT-ITEM-0005',
        'title': 'Academic Standard Curriculum Item #5',
        'department': 'Computer Science',
        'semester': 6,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 5',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.5: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.5: Architectural Implementation and Data Structures',
            'Topic 3.5: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.5: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 6',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 6,
        'code': 'CAT-ITEM-0006',
        'title': 'Academic Standard Curriculum Item #6',
        'department': 'Electronics & Comm',
        'semester': 7,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 6',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.6: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.6: Architectural Implementation and Data Structures',
            'Topic 3.6: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.6: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 7',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 7,
        'code': 'CAT-ITEM-0007',
        'title': 'Academic Standard Curriculum Item #7',
        'department': 'Information Tech',
        'semester': 8,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 7',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.7: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.7: Architectural Implementation and Data Structures',
            'Topic 3.7: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.7: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 8',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 8,
        'code': 'CAT-ITEM-0008',
        'title': 'Academic Standard Curriculum Item #8',
        'department': 'Mechanical Eng',
        'semester': 1,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 8',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.8: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.8: Architectural Implementation and Data Structures',
            'Topic 3.8: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.8: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 9',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 9,
        'code': 'CAT-ITEM-0009',
        'title': 'Academic Standard Curriculum Item #9',
        'department': 'Civil Eng',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 9',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.9: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.9: Architectural Implementation and Data Structures',
            'Topic 3.9: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.9: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 10',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 10,
        'code': 'CAT-ITEM-0010',
        'title': 'Academic Standard Curriculum Item #10',
        'department': 'Computer Science',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 10',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.10: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.10: Architectural Implementation and Data Structures',
            'Topic 3.10: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.10: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 1',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 11,
        'code': 'CAT-ITEM-0011',
        'title': 'Academic Standard Curriculum Item #11',
        'department': 'Electronics & Comm',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 11',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.11: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.11: Architectural Implementation and Data Structures',
            'Topic 3.11: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.11: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 2',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 12,
        'code': 'CAT-ITEM-0012',
        'title': 'Academic Standard Curriculum Item #12',
        'department': 'Information Tech',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 12',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.12: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.12: Architectural Implementation and Data Structures',
            'Topic 3.12: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.12: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 3',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 13,
        'code': 'CAT-ITEM-0013',
        'title': 'Academic Standard Curriculum Item #13',
        'department': 'Mechanical Eng',
        'semester': 6,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 13',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.13: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.13: Architectural Implementation and Data Structures',
            'Topic 3.13: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.13: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 4',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 14,
        'code': 'CAT-ITEM-0014',
        'title': 'Academic Standard Curriculum Item #14',
        'department': 'Civil Eng',
        'semester': 7,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 14',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.14: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.14: Architectural Implementation and Data Structures',
            'Topic 3.14: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.14: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 5',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 15,
        'code': 'CAT-ITEM-0015',
        'title': 'Academic Standard Curriculum Item #15',
        'department': 'Computer Science',
        'semester': 8,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 15',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.15: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.15: Architectural Implementation and Data Structures',
            'Topic 3.15: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.15: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 6',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 16,
        'code': 'CAT-ITEM-0016',
        'title': 'Academic Standard Curriculum Item #16',
        'department': 'Electronics & Comm',
        'semester': 1,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 16',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.16: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.16: Architectural Implementation and Data Structures',
            'Topic 3.16: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.16: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 7',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 17,
        'code': 'CAT-ITEM-0017',
        'title': 'Academic Standard Curriculum Item #17',
        'department': 'Information Tech',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 17',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.17: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.17: Architectural Implementation and Data Structures',
            'Topic 3.17: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.17: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 8',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 18,
        'code': 'CAT-ITEM-0018',
        'title': 'Academic Standard Curriculum Item #18',
        'department': 'Mechanical Eng',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 18',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.18: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.18: Architectural Implementation and Data Structures',
            'Topic 3.18: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.18: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 9',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 19,
        'code': 'CAT-ITEM-0019',
        'title': 'Academic Standard Curriculum Item #19',
        'department': 'Civil Eng',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 19',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.19: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.19: Architectural Implementation and Data Structures',
            'Topic 3.19: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.19: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 10',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 20,
        'code': 'CAT-ITEM-0020',
        'title': 'Academic Standard Curriculum Item #20',
        'department': 'Computer Science',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 20',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.20: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.20: Architectural Implementation and Data Structures',
            'Topic 3.20: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.20: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 1',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 21,
        'code': 'CAT-ITEM-0021',
        'title': 'Academic Standard Curriculum Item #21',
        'department': 'Electronics & Comm',
        'semester': 6,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 21',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.21: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.21: Architectural Implementation and Data Structures',
            'Topic 3.21: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.21: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 2',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 22,
        'code': 'CAT-ITEM-0022',
        'title': 'Academic Standard Curriculum Item #22',
        'department': 'Information Tech',
        'semester': 7,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 22',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.22: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.22: Architectural Implementation and Data Structures',
            'Topic 3.22: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.22: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 3',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 23,
        'code': 'CAT-ITEM-0023',
        'title': 'Academic Standard Curriculum Item #23',
        'department': 'Mechanical Eng',
        'semester': 8,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 23',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.23: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.23: Architectural Implementation and Data Structures',
            'Topic 3.23: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.23: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 4',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 24,
        'code': 'CAT-ITEM-0024',
        'title': 'Academic Standard Curriculum Item #24',
        'department': 'Civil Eng',
        'semester': 1,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 24',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.24: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.24: Architectural Implementation and Data Structures',
            'Topic 3.24: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.24: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 5',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 25,
        'code': 'CAT-ITEM-0025',
        'title': 'Academic Standard Curriculum Item #25',
        'department': 'Computer Science',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 25',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.25: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.25: Architectural Implementation and Data Structures',
            'Topic 3.25: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.25: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 6',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 26,
        'code': 'CAT-ITEM-0026',
        'title': 'Academic Standard Curriculum Item #26',
        'department': 'Electronics & Comm',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 26',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.26: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.26: Architectural Implementation and Data Structures',
            'Topic 3.26: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.26: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 7',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 27,
        'code': 'CAT-ITEM-0027',
        'title': 'Academic Standard Curriculum Item #27',
        'department': 'Information Tech',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 27',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.27: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.27: Architectural Implementation and Data Structures',
            'Topic 3.27: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.27: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 8',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 28,
        'code': 'CAT-ITEM-0028',
        'title': 'Academic Standard Curriculum Item #28',
        'department': 'Mechanical Eng',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 28',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.28: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.28: Architectural Implementation and Data Structures',
            'Topic 3.28: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.28: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 9',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 29,
        'code': 'CAT-ITEM-0029',
        'title': 'Academic Standard Curriculum Item #29',
        'department': 'Civil Eng',
        'semester': 6,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 29',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.29: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.29: Architectural Implementation and Data Structures',
            'Topic 3.29: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.29: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 10',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 30,
        'code': 'CAT-ITEM-0030',
        'title': 'Academic Standard Curriculum Item #30',
        'department': 'Computer Science',
        'semester': 7,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 30',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.30: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.30: Architectural Implementation and Data Structures',
            'Topic 3.30: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.30: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 1',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 31,
        'code': 'CAT-ITEM-0031',
        'title': 'Academic Standard Curriculum Item #31',
        'department': 'Electronics & Comm',
        'semester': 8,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 31',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.31: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.31: Architectural Implementation and Data Structures',
            'Topic 3.31: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.31: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 2',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 32,
        'code': 'CAT-ITEM-0032',
        'title': 'Academic Standard Curriculum Item #32',
        'department': 'Information Tech',
        'semester': 1,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 32',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.32: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.32: Architectural Implementation and Data Structures',
            'Topic 3.32: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.32: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 3',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 33,
        'code': 'CAT-ITEM-0033',
        'title': 'Academic Standard Curriculum Item #33',
        'department': 'Mechanical Eng',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 33',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.33: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.33: Architectural Implementation and Data Structures',
            'Topic 3.33: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.33: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 4',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 34,
        'code': 'CAT-ITEM-0034',
        'title': 'Academic Standard Curriculum Item #34',
        'department': 'Civil Eng',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 34',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.34: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.34: Architectural Implementation and Data Structures',
            'Topic 3.34: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.34: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 5',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 35,
        'code': 'CAT-ITEM-0035',
        'title': 'Academic Standard Curriculum Item #35',
        'department': 'Computer Science',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 35',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.35: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.35: Architectural Implementation and Data Structures',
            'Topic 3.35: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.35: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 6',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 36,
        'code': 'CAT-ITEM-0036',
        'title': 'Academic Standard Curriculum Item #36',
        'department': 'Electronics & Comm',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 36',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.36: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.36: Architectural Implementation and Data Structures',
            'Topic 3.36: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.36: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 7',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 37,
        'code': 'CAT-ITEM-0037',
        'title': 'Academic Standard Curriculum Item #37',
        'department': 'Information Tech',
        'semester': 6,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 37',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.37: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.37: Architectural Implementation and Data Structures',
            'Topic 3.37: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.37: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 8',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 38,
        'code': 'CAT-ITEM-0038',
        'title': 'Academic Standard Curriculum Item #38',
        'department': 'Mechanical Eng',
        'semester': 7,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 38',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.38: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.38: Architectural Implementation and Data Structures',
            'Topic 3.38: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.38: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 9',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 39,
        'code': 'CAT-ITEM-0039',
        'title': 'Academic Standard Curriculum Item #39',
        'department': 'Civil Eng',
        'semester': 8,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 39',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.39: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.39: Architectural Implementation and Data Structures',
            'Topic 3.39: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.39: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 10',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 40,
        'code': 'CAT-ITEM-0040',
        'title': 'Academic Standard Curriculum Item #40',
        'department': 'Computer Science',
        'semester': 1,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 40',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.40: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.40: Architectural Implementation and Data Structures',
            'Topic 3.40: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.40: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 1',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 41,
        'code': 'CAT-ITEM-0041',
        'title': 'Academic Standard Curriculum Item #41',
        'department': 'Electronics & Comm',
        'semester': 2,
        'credits': 2,
        'objectives': [
            'Understand core theoretical foundations of module 41',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.41: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.41: Architectural Implementation and Data Structures',
            'Topic 3.41: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.41: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 2',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 42,
        'code': 'CAT-ITEM-0042',
        'title': 'Academic Standard Curriculum Item #42',
        'department': 'Information Tech',
        'semester': 3,
        'credits': 3,
        'objectives': [
            'Understand core theoretical foundations of module 42',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.42: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.42: Architectural Implementation and Data Structures',
            'Topic 3.42: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.42: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 3',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 43,
        'code': 'CAT-ITEM-0043',
        'title': 'Academic Standard Curriculum Item #43',
        'department': 'Mechanical Eng',
        'semester': 4,
        'credits': 4,
        'objectives': [
            'Understand core theoretical foundations of module 43',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.43: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.43: Architectural Implementation and Data Structures',
            'Topic 3.43: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.43: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 4',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
    {
        'id': 44,
        'code': 'CAT-ITEM-0044',
        'title': 'Academic Standard Curriculum Item #44',
        'department': 'Civil Eng',
        'semester': 5,
        'credits': 1,
        'objectives': [
            'Understand core theoretical foundations of module 44',
            'Apply algorithmic reasoning to practical engineering problems',
            'Design scalable software/hardware architectures with verified outcomes'
        ],
        'syllabus_topics': [
            'Topic 1.44: Mathematical Formulation and Rigorous Proofs',
            'Topic 2.44: Architectural Implementation and Data Structures',
            'Topic 3.44: Optimization, Benchmarking and Performance Metrics',
            'Topic 4.44: Industry Case Studies and Modern Best Practices'
        ],
        'references': [
            'Standard Textbook of Higher Education, Vol. 5',
            'International Journal of Applied Technology, Issue 2024'
        ]
    },
]
