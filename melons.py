"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    def __init__(self, species, qty, country_code="US"):


        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price."""
        base_price = 5
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
  
    def get_total(self):
        normal_order = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return normal_order + 3
        else:
            return normal_order
