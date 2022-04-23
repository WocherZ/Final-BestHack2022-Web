from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class ExtendedUser(User):
    balance = models.DecimalField(max_digits=32,
                                  decimal_places=4,
                                  validators=[MinValueValidator(0)],
                                  default=0.0,
                                  )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class NewsCategories(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['name']


class Sources(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Источник новости'
        verbose_name_plural = 'Источники новостей'
        ordering = ['name']


class News(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField(
        default=timezone.now
    )
    source = models.ForeignKey(Sources,
                               on_delete=models.SET_NULL,
                               null=True
                               )
    text = models.TextField()
    short_text = models.CharField(max_length=512)
    category = models.ForeignKey(NewsCategories,
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return "Новость: " + str(self.name) + " " + str(self.date)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['date']


class Currencies(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=8)
    ico = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.code)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['code']


class CurrenciesRates(models.Model):
    first_currency = models.ForeignKey(Currencies,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name='first_currency'
                                       )
    second_currency = models.ForeignKey(Currencies,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        related_name='second_currency'
                                        )
    current_rate = models.DecimalField(
        max_digits=19,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0
    )


    def __str__(self):
        return str(self.second_currency.code) + "/" + str(self.first_currency.code)

    class Meta:
        verbose_name = 'Котировка'
        verbose_name_plural = 'Котировки'
        ordering = ['first_currency']


class UserProperties(models.Model):
    user = models.ForeignKey(ExtendedUser,
                             on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies,
                                 on_delete=models.SET_NULL,
                                 null=True)
    price = models.DecimalField(max_digits=19,
                                decimal_places=4,
                                validators=[MinValueValidator(0)],
                                default=0.0)
    number = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
    )

    def __str__(self):
        return str(self.user) + " " + str(self.currency)

    class Meta:
        verbose_name = 'Валюта пользователя'
        verbose_name_plural = 'Валюты пользователей'


class Organizations(models.Model):
    MARKUP_CHOICE = [
        ("%", 'в процентах'),
        ('.', 'абсолютное значение'),
    ]
    name = models.CharField(max_length=32)
    type_price_markup = models.CharField(
        max_length=3,
        choices=MARKUP_CHOICE
    )
    procent_markup = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
    )
    absolute_markup = models.DecimalField(
        max_digits=19,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0
    )
    currency = models.ManyToManyField(CurrenciesRates)

    def __str__(self):
        return "Организация: " + str(self.name)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class BalanceOperations(models.Model):
    BALANCE_OPERATIONS = [
        ('Пополнение', 'Пополнение'),
        ('Снятие', 'Снятие')
    ]
    user = models.ForeignKey(ExtendedUser,
                             on_delete=models.SET_NULL,
                             null=True
                             )
    type_balance_operation = models.CharField(
        max_length=16,
        choices=BALANCE_OPERATIONS,
    )
    date = models.DateTimeField(
        default=timezone.now
    )
    amount = models.DecimalField(max_digits=19,
                                 decimal_places=4,
                                 validators=[MinValueValidator(0)],
                                 default=0.0)

    def __str__(self):
        return str(self.type_balance_operation) + " " \
               + str(self.amount) + " " \
               + str(self.user)

    class Meta:
        verbose_name = 'Операция с балансом'
        verbose_name_plural = 'Операции с балансом'
        ordering = ['date']


class BuySellOperations(models.Model):
    BUY_SELL_OPERATIONS = [
        ('Покупка', 'Покупка'),
        ('Продажа', 'Продажа')
    ]
    user = models.ForeignKey(ExtendedUser,
                             on_delete=models.SET_NULL,
                             null=True
                             )
    type_buy_sell_operation = models.CharField(
        max_length=16,
        choices=BUY_SELL_OPERATIONS,
    )
    price = models.DecimalField(max_digits=19,
                                decimal_places=4,
                                validators=[MinValueValidator(0)],
                                default=0.0)
    number = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
    )
    currency = models.ForeignKey(Currencies,
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )
    date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return str(self.type_buy_sell_operation) \
               + " " + str(self.number) \
               + " " + str(self.currency) \
               + " " + str(self.user)


    class Meta:
        verbose_name = 'Операция покупки-продажи'
        verbose_name_plural = 'Операции покупки-продажи'
        ordering = ['date']
