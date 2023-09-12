from tortoise import fields, models

class Cat(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=120)
    color = fields.CharField(max_length=120, null=False)
    image = fields.CharField(max_length=120, null=False)
    created_at = fields.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.color}'
    
    class Meta:
        table = 'cat'
