# import datetime
# from enum import Enum
# from typing import Dict, List, Optional, Set

# from pydantic import BaseModel, Field, SecretStr

# from opyrator.components.types import FileContent


# class SelectionValue(str, Enum):
#     FOO = "foo"
#     BAR = "bar"


# class OtherData(BaseModel):
#     text: str
#     integer: int


# class ShowcaseModel(BaseModel):
#     short_text: str = Field(..., max_length=60, description="Short text property")
#     password: SecretStr = Field(..., description="Password text property")
#     long_text: str = Field(..., description="Unlimited text property")
#     integer_in_range: int = Field(
#         20,
#         ge=10,
#         lt=30,
#         multiple_of=2,
#         description="Number property with a limited range. Optional because of default value.",
#     )
#     positive_integer: int = Field(
#         ..., ge=0, multiple_of=10, description="Positive integer with step count of 10."
#     )
#     float_number: float = Field(0.001)
#     date: Optional[datetime.date] = Field(
#         datetime.date.today(),
#         description="Date property. Optional because of default value.",
#     )
#     time: Optional[datetime.time] = Field(
#         datetime.datetime.now().time(),
#         description="Time property. Optional because of default value.",
#     )
#     string_list: List[str] = Field(
#         ..., max_items=20, description="List of string values"
#     )
#     int_list: List[int] = Field(..., description="List of int values")
#     boolean: bool = Field(
#         False,
#         description="Boolean property. Optional because of default value.",
#     )
#     file_list: Optional[List[FileContent]] = Field(
#         None,
#         description="A list of files. Optional property.",
#     )
#     single_file: Optional[FileContent] = Field(
#         None,
#         description="A single file. Optional property.",
#     )
#     string_dict: Dict[str, str] = Field(
#         ..., description="Dict property with string values"
#     )
#     float_dict: Dict[str, float] = Field(
#         ..., description="Dict property with float values"
#     )
#     single_selection: SelectionValue = Field(
#         ..., description="Only select a single item from a set."
#     )
#     multi_selection: Set[SelectionValue] = Field(
#         ..., description="Allows multiple items from a set."
#     )
#     single_object: OtherData = Field(
#         ...,
#         description="Another object embedded into this model.",
#     )
#     object_list: List[OtherData] = Field(
#         ...,
#         description="A list of objects embedded into this model.",
#     )


# def showcase_components(input: ShowcaseModel) -> ShowcaseModel:
#     """Showcase of a variety of differnt property types and how they are shown in the UI.
#     This function only returns the input data.
#     """
#     return input


from enum import Enum
from tempfile import NamedTemporaryFile

# import fasttext
from pydantic import BaseModel, Field

from opyrator.components.types import FileContent


class Model(str, Enum):
    SKIPGRAM = "skipgram"
    CBOW = "cbow"


class LossFunction(str, Enum):
    NS = "ns"
    HS = "hs"
    SOFTMAX = "softmax"
    OVA = "ova"


class WordVectorTrainingInput(BaseModel):
    text: str = Field(
        ...,
        description="The text to use for training the word vector model.",
        min_length=10,
        max_length=5000,
    )
    model: Model = Field(
        Model.SKIPGRAM,
        title="Select Model Type",
        description="Model for computing word representations",
    )
    learning_rate: float = Field(0.05, gt=0.0, le=1)
    dimension: int = Field(50, ge=10, le=100, description="Size of word vectors.")
    epoch: int = Field(5, ge=1, le=20)
    min_count: int = Field(1, ge=1, description="Minimal number of word occurrences.")
    loss_function: LossFunction = Field(LossFunction.NS, title="Loss Function")


class WordVectorTrainingOutput(BaseModel):
    vector_file: FileContent


def train_word_vectors(input: WordVectorTrainingInput) -> WordVectorTrainingOutput:
    """Trains word vectors via [FastText](https://fasttext.cc) based on a provided text."""

    with NamedTemporaryFile(suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write(input.text)
        f.seek( 0)

        # model = fasttext.train_unsupervised(
        #     f.name,
        #     model=input.model.value,
        #     lr=input.learning_rate,
        #     dim=input.dimension,
        #     epoch=input.epoch,
        #     minCount=input.min_count,
        #     loss=input.loss_function,
        #     thread=1,  # only train with one thread to not block other demos
        # )

        # with NamedTemporaryFile(suffix=".vec", mode="w+b") as vec_file:
        #     words = model.get_words()
        #     for word in words:
        #         vec_file.write(
        #             str.encode(
        #                 word
        #                 + "".join(" " + str(vi) for vi in model.get_word_vector(word))
        #                 + "\n"
        #             )
        #         )
        #     vec_file.seek(0)
        #     return WordVectorTrainingOutput(vector_file=vec_file.read())

        return WordVectorTrainingOutput(vector_file=input.text)