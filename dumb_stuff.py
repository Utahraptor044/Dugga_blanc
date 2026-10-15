scatterplot = (
    ggplot(head_data, aes(x = 0))
    +geom_point(aes(y = 6), shape = 16 )
    +geom_point(aes(y = 7), shape = 1)
    + ggtitle("Comparaison des valeurs par gène")
    + xlab("Gènes")
    + ylab("Valeur")
    + theme(axis_text_x=element_text(rotation=90))
)
scatterplot.save(
    filename="scatterplot.png",
    width=10,
    height=6,
    dpi=300
)