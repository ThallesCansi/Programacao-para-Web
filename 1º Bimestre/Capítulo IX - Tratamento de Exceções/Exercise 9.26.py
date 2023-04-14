import mymodule # type: ignore

try:
    result = mymodule.myfunction()
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")