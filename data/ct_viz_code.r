setwd('C://Users//garrett//Dropbox//aa projects//PSYCHOPY DATA (1)//choootooo')

datafull <- read.csv('CTdata.csv')


ggplot(datafull, aes(x = trial, y = rt)) + geom_point(shape=1) + geom_smooth() +
  theme(plot.title = element_text(size=36, face="bold", vjust=2),
	axis.title.y = element_text(size=26,vjust = 1.5),
	axis.text.y = element_text(size=18, color = 'black'),
	axis.title.x = element_text(size=26,vjust = -.5),
	axis.text.x = element_text(size = 18, color = 'black')) +
  scale_y_continuous(limits = c(0,70), breaks = seq(0, 65, 10), name = 'Response Time') +
  scale_x_continuous(limits= c(0,59), breaks = seq(0, 59, 5), name = 'Trial')


ggplot(datafull, aes(x = trial, y = sel_taxo)) + geom_point(shape=1) + geom_smooth()
ggplot(datafull, aes(x = trial, y = sel_them)) + geom_point(shape=1) + geom_smooth()


ggplot(aggregate(sel_taxo ~ trial, mean, data = datafull), aes(x = trial, y = sel_taxo)) +
  geom_point(shape = 1) + geom_smooth() +
  theme(plot.title = element_text(size=36, face="bold", vjust=2),
	axis.title.y = element_text(size=26,vjust = 1.5),
	axis.text.y = element_text(size=18, color = 'black'),
	axis.title.x = element_text(size=26,vjust = -.5),
	axis.text.x = element_text(size = 18, color = 'black')) +
  scale_y_continuous(limits = c(0,1.00),breaks = seq(0, 1, 0.1), name = 'Proportion of Taxonomic Matches') +
  coord_cartesian(ylim = c(0.5,0.9)) 


ggplot(aggregate(sel_them ~ trial, mean, data = datafull), aes(x = trial, y = sel_them)) +
  geom_point(shape = 1) + geom_smooth() +
  theme(plot.title = element_text(size=36, face="bold", vjust=2),
	axis.title.y = element_text(size=26,vjust = 1.5),
	axis.text.y = element_text(size=18, color = 'black'),
	axis.title.x = element_text(size=26,vjust = -.5),
	axis.text.x = element_text(size = 18, color = 'black')) +
  scale_y_continuous(limits = c(0,1.00),breaks = seq(0, 1, 0.1), name = 'Proportion of Thematic Matches') +
  coord_cartesian(ylim = c(0.1,0.5))


ggplot(aggregate(rt ~ word_1, median, data = subset(datafull, subest = (sel_taxo == 1))),
  aes(reorder(word_1, rt), rt)) + geom_point(shape=1) +
  theme(plot.title = element_text(size=36, face="bold", vjust=2),
	axis.title.y = element_text(size=26,vjust = 1.5),
	axis.text.y = element_text(size=18, color = 'black'),
	axis.title.x = element_text(size=26,vjust = -.5),
	axis.text.x = element_text(size = 12, color = 'black', angle = 90, vjust = .025)) +
  scale_y_continuous(breaks = seq(4, 9.5, 0.5), name = 'Median Response Time') +
  scale_x_discrete(name = 'Base Word') +
  coord_cartesian(ylim = c(4,9.5))  
  

ggplot(aggregate(sel_taxo ~ cond + pid, mean, data = datafull), aes(x = as.factor(cond), y = sel_taxo)) +
  geom_boxplot(outlier.colour = 'red') + 
  geom_jitter(alpha=.7, position = position_jitter(width = .3, height = 0)) +
  theme(plot.title = element_text(size=36, face="bold", vjust=2),
	axis.title.y = element_text(size=26,vjust = 1.5),
	axis.text.y = element_text(size=18, color = 'black'),
	axis.title.x = element_text(size=26,vjust = -.5),
	axis.text.x = element_text(size = 18, color = 'black')) + 
  scale_y_continuous(limits=c(0,1.001),breaks=seq(0, 1, 0.1), name = 'Mean Taxonomic Matches') + 
  scale_x_discrete(name = 'Condition', breaks = c('1','2'), labels = c('Alike','Alien')) + 
  coord_cartesian(ylim = c(0,1))  

