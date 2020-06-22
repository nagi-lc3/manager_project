from django.db import models


class Person(models.Model):
    """人モデル"""

    class Meta(object):
        db_table = 'person'

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    # 名前
    name = models.CharField(verbose_name='名前', max_length=128)
    # 誕生日
    birthday = models.DateTimeField(verbose_name='誕生日')
    # 性別
    sex = models.IntegerField(verbose_name='性別')
    # 出身地
    address_from = models.IntegerField(verbose_name='出身地')
    # 現住所
    current_address = models.IntegerField(verbose_name='現住所')
    # メールアドレス
    email = models.EmailField(verbose_name='メールアドレス')

    def __str__(self):
        return self.name


class Manager(models.Model):
    """担当上司モデル"""

    class Meta(object):
        db_table = 'manager'

    # 部署の定数
    DEP_ACCOUNTING = 0  # 経理
    DEP_SALES = 5  # 営業
    DEP_PRODUCTION = 10  # 製造
    DEP_DEVELOPMENT = 15  # 開発
    DEP_HR = 20  # 人事
    DEP_FIN = 25  # 財務
    DEP_AFFAIRS = 30  # 総務
    DEP_PLANNING = 35  # 企画
    DEP_BUSINESS = 40  # 業務
    DEP_DISTR = 45  # 流通
    DEP_IS = 50  # 情報システム

    # 人
    person = models.ForeignKey(Person, verbose_name='人', on_delete=models.PROTECT)
    # 部署
    department = models.IntegerField(verbose_name='部署')
    # 着任時期
    joined_at = models.DateTimeField(verbose_name='着任時期')
    # やめた時期
    quited_at = models.DateTimeField(verbose_name='やめた時期', null=True, blank=True)

    def __str__(self):
        return str(self.person)


class Worker(models.Model):
    """労働者モデル"""

    class Meta(object):
        db_table = 'worker'

    # 人
    person = models.ForeignKey(Person, verbose_name='人', on_delete=models.PROTECT)
    # 着任時期
    joined_at = models.DateTimeField(verbose_name='着任時期')
    # やめた時期
    quited_at = models.DateTimeField(verbose_name='やめた時期', null=True, blank=True)
    # 担当上司
    manager = models.ForeignKey(Manager, verbose_name='担当上司', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.person)
