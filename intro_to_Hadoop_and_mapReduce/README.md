# intro_to_hadoop

### 用Hadoop/MapReuce来处理论坛数据是好的嘛？
这取决于我们对什么样子的数据感兴趣。

如果说数据已经存在在关系数据库管理系统（RDBMS)当中，并且你需要的信息已经在RDBMS中已经以一种方便检索的方式存储。这样就不值得再将数据额外导出并且存在Hadoop/MapReduce当中，
还需要根据你所需要收集的统计信息书写程序，通过运行这些程序才能够获得你所需要的数据的统计信息。

例如， stackExchange 数据查询。它有多种查询可以显示用户的行为信息，并且不需要用到MapReduce，而只是标准的SQL查询。

也就是说，如果你想要获得用户发布的内容，或者是有一些数据在默认的情况下并没有结构化（或者说这些数据的来源都不相同），利用MapReduce/Hadoop这的确是个好的方法。
但是，即使如此，存储在RDBMS当中仍然可以让数据有效的运行（could go a long way in providing that functionality)

最后，当数据被分散在不同的机器当中的时候，这些数据来源不同并且都没有结构。而且，你也没有存储在RDBMS中的数据。如果说获得的数据是这些，那么就是说这些数据可能都是没有结构化的。

**也就是说，做决定之前先要明确下面几个步骤：**
* 这些数据存在与哪里？是否已经存在在RDBMS当中？如果没有存在，那么MapReuce可能是好的选择。
* 这些数据是结构化的嘛（structured）？不是，那么MapReduce可能运作良好。
* 对这些数据加结构困难吗？
* 你是否有能够书写你想要获取数据的任何信息的代码的能力？  

如果说这些答案都倾向于支持MapReduce，那么就可以选择MapReduce了。

### 如何提高查找的有效性：
有一些显著的提升，例如让用户依照tags或者是发布/问题（posts/questions)查找。

我们不仅可以通过关键词查找，也可以通过将索引添加某些权重值进行查找。例如， 拥有好的信誉（reputation）的用户的问题或者答案可以认为质量是更好的。 我们可以通过将用户的数据库
和发布的数据库组合（也就是forum_user和forum_node组合），并且添加这些信息到索引。一旦这个索引建立， 搜索引擎就可以根据新的标准进行选择排序。显然， 有多种扩展的方法和
权重可以添加， 例如问题或这回答被顶的（upvote）或者被踩的次数等。

### hankering查看问题长度和回复的平均长度的相关性。