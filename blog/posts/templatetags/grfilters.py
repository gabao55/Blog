from django import template

register = template.Library()

@register.filter(name='comments_plural')
def comments_plural(comments_number):
    try:
        comments_number = int(comments_number)

        if comments_number == 0:
            return 'No comments'
        elif comments_number == 1:
            return f'{comments_number} comment'
        else:
            return f'{comments_number} comments'

    except:
        return f'{comments_number} comment(s)'