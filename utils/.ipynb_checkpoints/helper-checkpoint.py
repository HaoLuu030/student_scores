
def check_capping(column, display_head=True, rows=5):
    if display_head:
        return column.value_counts().sort_index().head(rows).rename('count').reset_index()
    else:
        return column.value_counts().sort_index().tail(rows).rename('count').reset_index()