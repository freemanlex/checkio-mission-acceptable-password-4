"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["short"],
            "answer": False
        },
        {
            "input": ["short54"],
            "answer": True
        },
        {
            "input": ["muchlonger"],
            "answer": True
        },
        {
            "input": ["ashort"],
            "answer": False
        },
        {
            "input": ["notshort"],
            "answer": False
        },
        {
            "input": ["muchlonger5"],
            "answer": True
        },
        {
            "input": ["sh5"],
            "answer": False
        },
        {
            "input": ["1234567"],
            "answer": False
        },
        {
            "input": ["12345678910"],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": ["this is password"],
            "answer": True
        }
    ]
}