<font size=4>咱们从一个实际例子聊起：**说，一个大富豪想要买车**</font>

<font size=3>首先定义个通用的人类与车类 人会开车，车被人开：

```python
class Human:
    def __init__(self, name):
        self.name = name

    def drive_a_car(self, car):
        print(f'{self.name} is driving a {car.brand} car!!!')


class Car:
    def be_drived(self, human):
        human.drive_a_car(self)
```

具体的奔驰车类、福特车类：

```python
class Benz(Car):
    # 继承于车类，所以也能被开
    def __init__(self, brand, engine, tyre):
        self.brand = brand
        self.engine = engine
        self.tyre = tyre


class Ford(Car):
    def __init__(self, brand, engine, tyre):
        self.brand = brand
        self.engine = engine
        self.tyre = tyre

```

</font>

## <font size=3 color=purple>场景1 ：最早期，福特、奔驰都是派工程师们出差过来给你装个车</font>

<font size=3>&nbsp; &nbsp; 他们要求富豪负责买好各类轮胎、各类引擎，配件都准备好了，然后派工程师们给你咔咔组装出来一辆车。

&nbsp; &nbsp; 富豪傻了，这他哪懂采购啥好啊，就算懂，他每次买辆福特车，哪怕和上回一样配置的，也得贼麻烦地买一遍配件。就类比成如下代码

```python
richMan = Human('July')
# 富豪要一五一十准备好brand、engine、tyre：
a_Benz_car = Benz('Benz', 'Engine2T', 'Micillin')
a_Ford_car = Ford('Ford', 'Engine1T', 'Micillin')
richMan.drive(a_Benz_car)
richMan.drive(a_Ford_car)
```

&nbsp; &nbsp; 后来福特、奔驰发现没必要啊，咱们找代工厂啊，啥车用啥料，定好了，富豪就不需要学这门学问，会开会用就行，于是各个厂子找了代工厂帮自己装车，产生下面的改造：

```python
class CarFactory:
    def makeACar(self, brand):
        if brand == 'Benz':
            return Benz(brand=brand, engine='Engine2T', tyre='Micillin')
        elif brand == 'Ford':
            return Ford(brand=brand, engine='Engine1T', tyre='Micillin')


richMan = Human('July')
小鞠车业 = CarFactory()
a_Benz_car = 小鞠车业.makeACar('Benz')
a_Ford_car = 小鞠车业.makeACar('Ford')
richMan.drive(a_Benz_car)
richMan.drive(a_Ford_car)
```

&nbsp; &nbsp; 到这里的改造就是简单工厂模式，也即静态工厂。使得消费端不需要知道产品端的构造细节，也即富豪不需要学习啥车是怎么造的，反正造车厂明白就行。</font>

## <font size=3 color=purple>场景2：富豪这边舒服了，但是造车厂每次头都忙炸了，N多个厂商要找他代工</font>

<font size=3>
&nbsp; &nbsp; 这哪行啊，而且造的不好还被罚钱，厂商们的单独自定义特点还多的要死，这个要能潜水，那个要能上天。。。得了，我造车厂搞分厂，只给单一品牌造车，也处理得好各品牌的脾气。

```python
class CarFactory:
    def makeACar(self): pass


class BenzFactory(CarFactory):
    def makeACar(self, engine='Engine2T', tyre='Micillin'):
        # 奔驰厂自己的造车流水线，品牌一定是奔驰了，引擎、轮胎有默认配置，买方无需关心
        return Benz(brand='Benz', engine=engine, tyre=tyre)


class FordFactory(CarFactory): 
    def makeACar(self, engine='Engine1T', tyre='Micillin'):
        # 福特厂自己的造车流水线，品牌一定是福特，引擎、轮胎有默认配置，买方无需关心
        return Benz(brand='Ford', engine=engine, tyre=tyre)


richMan = Human('July')
小鞠车业_奔驰 = BenzFactory()
小鞠车业_福特 = FordFactory()
a_Benz_car = 小鞠车业_奔驰.makeACar()
a_Ford_car = 小鞠车业_福特.makeACar()
richMan.drive(a_Benz_car)
richMan.drive(a_Ford_car)
```

&nbsp; &nbsp; 这就是工厂模式了，也即多态工厂，处理简单工厂处理不了的自定义问题。简单工厂要求造出来的产品很大程度上相似（我只让你选轮胎类型，轮胎个数不允许改，就得是4个），但是实际情况是很复杂的，并不是所有工厂只生产4轮子的车子，2轮子自行车、8轮子的卡车，没有个性化的话，简单工厂模式就很鸡肋了。

&nbsp; &nbsp; 思考一下使用了工厂模式，我想往系统里录入新的车品牌，录入个五菱宏光、奥迪、宝马，都会非常非常轻松。继承CarFactory，生成自己宝马牌子的CarFactory就行。</font>

## <font size=3 color=purple>场景3：福特、奔驰在卖车行业赚的风生水起了，于是想入伙军工业，造坦克</font>

<font size=3>&nbsp; &nbsp; 福特、奔驰想找专门组装坦克的重工业厂，他们找到了造车厂所属的重工制造业公司列表，找到了个专门做重工的，于是老套路，又让重工厂开设了福特、奔驰的重工坦克分厂

```python
class VehicalFactory:
    pass


class BenzVehicalFactory(VehicalFactory):
    pass


class FordVehicalFactory(VehicalFactory):
    pass


class BenzTankFactory(BenzVehicalFactory):
    def makeATank(self): ...


class BenzCarFactory(BenzVehicalFactory):
    def makeACar(self): ...


class FordTankFactory(FordVehicalFactory):
    def makeATank(self): ...


class FordCarFactory(FordVehicalFactory):
    def makeACar(self): ...


richMan = Human('July')
小鞠车业_奔驰 = BenzCarFactory()
小鞠车业_福特 = FordCarFactory()
小张重工_奔驰 = BenzTankFactory()
小张重工_福特 = FordTankFactory()
a_Benz_car = 小鞠车业_奔驰.makeACar()
a_Ford_car = 小鞠车业_福特.makeACar()
a_Benz_tank = 小张重工_奔驰.makeATank()
a_Ford_tank = 小张重工_福特.makeATank()
richMan.drive(a_Benz_car)
richMan.drive(a_Ford_car)
richMan.drive(a_Benz_tank)
richMan.drive(a_Ford_tank)
```
&nbsp; &nbsp; 这就是抽象工厂模式，在保留产品定制化的前提下，完成了开辟新产品族的重任。我们从实际生产的产品出发，可以观察抽象工厂模式的组成结构：
1.  管理、生产工厂的*抽象工厂制造类*
2.  被1生产出来的，实际的不同定制化工厂
3.  同一个定制化的工厂里，又能生产出不同产品的*抽象产品制造类*
4.  被3生产出来的，实际的同工厂不同产品

&nbsp; &nbsp; 可能有点绕啊，不过这才是抽象工厂模式。

&nbsp; &nbsp; 然后谈谈它的优点：刚刚说到工厂模式好扩展新的造车品牌，五菱宏光、宝马很轻松得能加入系统中；那么抽象工厂模式就做到了，造飞机的、造火箭、造船的不同品牌也能录入系统，只是他们不要CarFactory，而要PlaneFactory、RocketFactory、BoatFactory就行，这点是工厂模式做不到的。是不是扩展性又上升一个层次？

&nbsp; &nbsp; 因此做个总结</font>

| --- | 简单工厂             | 工厂模式           | 抽象工厂                         |
| ---- | -------------------- | ------------------ | -------------------------------- |
| 优点 | 解耦了产品端与用户端，分工明确 | 解决了产品定制化的难题，能够扩展更多同类型工厂 | 扩展产品族成为可能，可以录入不同类型的工厂了 |
| 缺点 | 产品端逻辑压力很大，定制难处理   | 不宜添加新的产品族 | 每次添加产品族都需要写多个抽象类要再编写一次   |