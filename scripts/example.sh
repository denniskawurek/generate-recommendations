#!/bin/bash

echo '[
    {
        "id": 1,
        "content": "This is just an example in one file."
    }
]' > res/1.json


echo '[
    {
        "id": 2,
        "content": "This is an example."
    },
    {
        "id": 3,
        "content": "Also a second example."
    }
]' > res/2.json

python main.py --content_identifier "content" --top_identifier "id"  res/1.json res/2.json

more out/top_5.json | jq 