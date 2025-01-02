# Calculate similarities betweens JSON objects

This calculates the similarities between JSON objects and returns a file with top x entries.

Can be used to generate recommendations for similar blog posts.

## Setup

```sh
python -m spacy download en_core_web_lg
pip install tensorflow_hub
```

Requires Python 3.12.

Install requirements from `requirements.txt`:

```sh
pip install -r requirements.txt
```

Install the [en_core_web_lg model](https://spacy.io/models/en) (license: MIT):

```sh
python -m spacy download en_core_web_lg
```

This uses [universal-sentence-encoder](https://www.kaggle.com/models/google/universal-sentence-encoder/tensorFlow2/universal-sentence-encoder/2) (license: Apache 2.0).


## Example usage

The following command calculates similarities between all objects in the two given JSON files and outputs all top 5 similarities in one JSON file.

```sh
python main.py --content_identifier "content" --highlights_identifier "id" 1.json 2.json
```

### Explanation of field usage

With the command above the similarity of the `content` field in all objects will be calculated.

The result is a json file with top x similarities between them, ordered and identified by the `id` field.

`1.json`:

```json
[
    {
        "id": 1,
        "content": "This is just an example in one file."
    }
]
```

`2.json`:

```json
[
    {
        "id": 2,
        "content": "This is an example."
    },
    {
        "id": 3,
        "content": "Also a second example."
    }
]
```

Result `top_5.json`:

```json
{
    "1": [
        {
            "id": 2,
            "content": "example."
        },
        {
            "id": 3,
            "content": "second example."
        }
    ],
    "2": [
        {
            "id": 3,
            "content": "second example."
        },
        {
            "id": 1,
            "content": "example one file."
        }
    ],
    "3": [
        {
            "id": 2,
            "content": "example."
        },
        {
            "id": 1,
            "content": "example one file."
        }
    ]
}
```

Please note that the field `content` is sanitized and can differ from the input.

You can run this with `scripts/example.sh`.