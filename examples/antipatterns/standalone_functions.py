"""
This module demonstrates two approaches for adding additional
functions/methods to your Frameworks. The first approach(the anti-pattern)
defines the discount function as a standalone function, which can lead to
unintended side-effects by operating outside the encapsulated context of the
class instance. The second approach integrates the discount logic as an
instance method within the Travel2021 class, making the behavior safer and
more predictable by confining its scope to the class instance.

Key Points:
    - Standalone function (anti-pattern):
        - Defined outside any class, which increases the risk of unexpected
            side-effects if the function is modified or if it inadvertently
            manipulates shared state.
        - Lacks access to instance-specific attributes, reducing cohesion in
            the design.
    - Instance method (preferred pattern):
        - Encapsulated within the Travel2021 class, ensuring it operates on
            the instance's own data.
        - Enhances maintainability and predictability, as changes to the
            method only affect the specific class implementation.
"""

from sentinelpricing import Framework, Rate


# ------------------------------
# ANTI-PATTERN: Standalone function
# ------------------------------
def apply_group_discount(quote):
    """
    Applies a group discount to the given quote based on the number of
    travellers.

    Args:
        quote (dict or a compatible object): The quote data that supports
            arithmetic operations and contains a 'number_of_travellers' key.

    Returns:
        The modified quote after applying the group discount, if applicable.

    Note: This function is defined outside of any class, which can lead to
        side-effects. Since it is not bound to a particular instance, its
        behavior might be inadvertently affected by external changes or
        modifications, reducing code clarity and safety.
    """
    group_discount = Rate("Group Discount", 0.8)
    # If more than 2 travellers, apply discount by multiplying the quote.
    if quote["number_of_travellers"] > 2:
        return quote * group_discount
    return quote


class Travel2021(Framework):
    """
    Travel2021 pricing model for the year 2021 that calculates the insurance
    quote.

    This version demonstrates the anti-pattern by calling the
    standalone 'apply_group_discount' function, which may cause side-effects
    by relying on external function state rather than being encapsulated
    within the class.
    """

    def setup(self):
        # Set up the base net rate for the insurance quote.
        self.net_rate = Rate("Net Rate", 300)
        # Define region-specific multipliers.
        self.region = {
            "USA": Rate("Region: USA", 2.5),
            "Non-USA": Rate("Region: USA", 1),
        }

    def calculation(self, quote):
        # Start with adding the base net rate.
        quote += self.net_rate
        # Multiply the quote by the appropriate region rate.
        quote *= self.region
        # Apply the group discount using the standalone function.
        # This external function call may inadvertently affect or be affected
        # by other parts of the system.
        quote = apply_group_discount(quote)
        return quote


class Travel2022(Travel2021):
    """
    Travel2022 pricing model for the year 2022.

    Similar to Travel2021, it uses the standalone group discount function,
    which is less safe due to potential side-effects.
    """

    def setup(self):
        self.net_rate = Rate("Net Rate", 400)

    def calculation(self, quote):
        quote += self.net_rate
        quote *= self.region
        quote = apply_group_discount(quote)
        return quote


class Travel2023(Travel2022):
    """
    Travel2023 pricing model for the year 2023.

    This class also relies on the standalone discount function, making it
    prone to similar side-effect issues as Travel2021 and Travel2022.
    """

    def setup(self):
        self.net_rate = Rate("Net Rate", 400)

    def calculation(self, quote):
        quote += self.net_rate
        quote *= self.region
        quote = apply_group_discount(quote)
        return quote


# ------------------------------
# PREFERRED PATTERN: Instance method
# ------------------------------
class Travel2021Safely(Framework):
    """
    Travel2021Safely pricing model for the year 2021.

    This version integrates the group discount logic as an instance method,
    which enhances encapsulation and reduces the risk of side-effects. By
    keeping the discount logic within the class, it only affects and is
    affected by the instance's own data, making the system easier to
    understand and maintain.
    """

    def setup(self):
        # Initialize the base net rate for the insurance quote.
        self.net_rate = Rate("Net Rate", 300)
        # Define region-specific multipliers.
        self.region = {
            "USA": Rate("Region: USA", 2.5),
            "Non-USA": Rate("Region: USA", 1),
        }

    def apply_group_discount(self, quote):
        """
        Applies a group discount to the given quote based on the number of
        travellers.

        Being an instance method, it encapsulates the discount logic within
        the class context. This limits the scope of its effects to the
        instance and avoids unintended interactions with external state.

        Args:
            quote (dict or a compatible object): The quote data that supports
                arithmetic operations and contains a 'number_of_travellers'
                key.

        Returns:
            The modified quote after applying the group discount, if
                applicable.
        """
        group_discount = Rate("Group Discount", 0.8)
        if quote["number_of_travellers"] > 2:
            return quote * group_discount
        return quote

    def calculation(self, quote):
        # Add the net rate to the quote.
        quote += self.net_rate
        # Multiply the quote by the region multiplier.
        quote *= self.region
        # Apply the group discount using the encapsulated instance method.
        # This approach confines the discount logic to the class, preventing
        # external modifications.
        quote = self.apply_group_discount(quote)
        return quote


class Travel2022Safely(Travel2021Safely):
    """
    Travel2022Safely pricing model for the year 2022.

    Although it calls the group discount function similarly to previous
    versions, in a complete implementation it would benefit from having its
    own properly encapsulated discount logic.
    """

    def setup(self):
        self.net_rate = Rate("Net Rate", 400)

    def calculation(self, quote):
        quote += self.net_rate
        quote *= self.region
        # For demonstration, if Travel2022 were updated to use the instance
        # method, it might look like:
        quote = self.apply_group_discount(quote)
        return quote


class Travel2023Safely(Travel2022Safely):
    """
    Travel2023Safely pricing model for the year 2023.

    Like Travel2022Safely, this class is provided for structural consistency.
    In a real-world scenario, each class would encapsulate its own logic to
    ensure that side-effects are minimized.
    """

    def setup(self):
        self.net_rate = Rate("Net Rate", 400)

    def calculation(self, quote):
        quote += self.net_rate
        quote *= self.region
        # Similar note applies here regarding encapsulated discount logic.
        quote = self.apply_group_discount(quote)
        return quote
