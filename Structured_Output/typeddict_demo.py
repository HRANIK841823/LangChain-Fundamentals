from typing import TypedDict

class ProductReview(TypedDict):
    product_name: str
    rating: int
    review:str


#TypedDict Donot gives us error when we input and string in the place of a int
#No Validation

new_review: ProductReview={
    "product_name":"Wireless keyboard",
    "rating":"Excellent",
    "review":"Excellent Product"
}

print(new_review)