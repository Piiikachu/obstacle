library("ggplot2")

#read file
df<-read.table("../3-6.surf",header = TRUE,sep = ' ')

#sort by id
df<-df[sort(df$SURFS_id,index.return=TRUE)$ix,]

#delete extra columns
df$X<-NULL

#calculate center point
df$x1<-(df$v1x+df$v2x)/2
df$y1<-(df$v1y+df$v2y)/2



#seprate into surface
dfs1<-df[1:80,]

?ggplot()


rm(df2)

?rep()
?data.frame

ggplot(dfs1,aes(x1,f_2.2.))+geom_line()+geom_point()

rm(p)

qplot(v1x,f_2.2.,data=dfs1,geom='line')
