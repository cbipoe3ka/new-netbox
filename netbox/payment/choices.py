from utilities.choices import ChoiceSet

class PaymentPeriodChoices(ChoiceSet):

    PAYMENT_YEAR = 'yearly'
    PAYMENT_MONTH =  'monthly'
    PAYMENT_ONE = 'one'
    CHOICES = (
        (PAYMENT_YEAR, 'yearly'),
        (PAYMENT_MONTH, 'monthly'),
        (PAYMENT_ONE, 'one'),
    )

    LEGACY_MAP = {
        PAYMENT_YEAR: 0,
        PAYMENT_MONTH: 1,
        PAYMENT_ONE: 2,
    }


class PaymentTypeChoices (ChoiceSet):

    TYPE_RENT = 'Rent'
    TYPE_PENALTY = 'Penalty'
    TYPE_BUY = 'Buying'
    TYPE_MAINTENANCE = 'Maintenance'
    TYPE_REPAIR = 'Repair'

    CHOICES = (
        (TYPE_RENT, 'Rent'),
        (TYPE_PENALTY, 'Penalty'),
        (TYPE_BUY, 'Buying'),
        (TYPE_MAINTENANCE, 'Maintenance'),
        (TYPE_REPAIR, 'Repair'),
    )

    LEGACY_MAP = {
        TYPE_RENT: 0,
        TYPE_PENALTY: 1,
        TYPE_BUY: 2,
        TYPE_MAINTENANCE: 3,
        TYPE_REPAIR: 4,
    }


class CurrencyChoices (ChoiceSet):
    DOLLAR = 'USD'
    EURO = 'EUR'
    RUB = 'RUB'
    DRAM = 'AMD'

    CHOICES = (
        (DOLLAR, 'USD'),
        (EURO,'EUR'),
        (RUB, 'RUB'),
        (DRAM, 'AMD'),
    )

    LEGACY_MAP = {
        DOLLAR: 0,
        EURO: 1,
        RUB: 2,
        DRAM: 3,
    }


class SubProjectChoices (ChoiceSet):
    STUDIO = 'Студия'
    TENNIS = 'Теннис'

    CHOICES = (
        (STUDIO, 'Студия'),
        (TENNIS, 'Теннис'),
    )


    LEGACY_MAP = {
        STUDIO: 0,
        TENNIS: 1,
    }