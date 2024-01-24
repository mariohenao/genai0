from semantic_kernel.plugin_definition import sk_function
from semantic_kernel.sk_pydantic import SKBaseModel

class OpsPlugin(SKBaseModel):
    """
    OpsPlugin provides functions to make operations on texts and numbers.

    Usage:
        kernel.import_plugin(OpsPlugin(), plugin_name="ops")

    Examples:
        SKContext["input"] = "  hello \nworld  "
        {{text.count_words $input}} => 2

        SKContext["input"] = 2
        {{number.two_to_the $input}} => 4
    """

    @sk_function(description="Counts the number of words in a verse.")
    def count_words(self, text: str) -> str:
        """
        Counts the number of words in a verse.

        Example:
            SKContext["input"] = "  hello \nworld  "
            {{text.count_words $input}} => 2
        """
        words = text.split()
        return str(len(words))

    @sk_function(description="Computes the number 2 to the argument power.")
    def two_to_the(self, number: str) -> str:
        """
        Computes the number 2 to the argument power.

         Example:
             SKContext["input"] = "2"
             {{number.two_to_the $input}} => 4
        """
        return str(2 ** int(number))