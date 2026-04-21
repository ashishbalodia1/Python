
# To import function from another package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping, calc_taxes

calc_shipping()
calc_taxes()

