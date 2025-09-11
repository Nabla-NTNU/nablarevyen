from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    published = models.BooleanField(
        default=False, help_text="Set this to publish position item."
    )
    open = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"


class Application(models.Model):
    position = models.ForeignKey(
        "Position", on_delete=models.CASCADE, verbose_name="Opptak"
    )
    name = models.CharField(max_length=200, verbose_name="Navn")
    email = models.EmailField(verbose_name="Epostadresse")
    phone = models.CharField(max_length=20, verbose_name="Telefonnummer")
    student_class = models.PositiveIntegerField(verbose_name="Klasse")
    text = models.TextField(verbose_name="Søknadstekst")
    first_group = models.ForeignKey(
        "groups.Group",
        on_delete=models.SET_NULL,
        related_name="applications_first",
        null=True,
        blank=True,
        default="",
        verbose_name="Førstevalg",
    )
    second_group = models.ForeignKey(
        "groups.Group",
        on_delete=models.SET_NULL,
        related_name="applications_second",
        null=True,
        blank=True,
        default="",
        verbose_name="Andrevalg",
    )
    third_group = models.ForeignKey(
        "groups.Group",
        on_delete=models.SET_NULL,
        related_name="applications_third",
        null=True,
        blank=True,
        default="",
        verbose_name="Tredjevalg",
    )

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.position.title, self.name)

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
