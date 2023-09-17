def many_to_many(product=None, category=None, relation=None):
    return product.join(
        relation,
        product.id==relation.product,
        'left_outer',
        ).join(
            category,
            relation.category==category.id,
            'left_outer',
            ).select(product.name, category.name).collect()

# На сколько я понял из задания в функцию приходит три датафрема к котром можно 
# сразу применять методы pyspark, сделав join между таблицами и вернуть 
# нужные колонки.