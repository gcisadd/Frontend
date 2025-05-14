1. 关于绝对定位、固定定位、相对定位和静态定位，下列说法错误的是( )

   A. 固定定位的元素会跟随浏览器滚动条进行滚动

   B. 绝对定位的元素会参考设置了定位(非静态)的父元素或者祖级元素进行定位对齐

   C. 静态定位是元素的默认定位方式，不需要设置

   D. 相对定位的元素保留自身在标准流中的位置，并且为绝对定位的子元素提供参考



2. 关于绝对定位、固定定位、相对定位和静态定位，下列说法正确的是( )

   A. 固定定位会参考设置了定位的父元素进行对齐

   B. 相对定位会参考元素本身在标准流以前的位置进行定位

   C. 静态定位可以设置 top 、left、right、 bottom值

   D. 绝对定位只会根据浏览器可视区域定位



3. 下列关于定位属性及特点说法正确的是 ( )

   A. 绝对定位的元素会参考设置了相对定位的父元素进行定位

   B. 固定定位会参考设置了定位的父元素进行定位

   C. 相对定位是指元素相对浏览器的可视区进行定位

   D. 设置了绝对定位的行内元素不能设置高度和垂直方向的内外边距



4. 以下选项，哪个是相对定位属性( )

   A. position: static;

   B. position: relative;

   C. position: absolute;

   D. position: fixed;



5. 以下关于相对定位的描述，合理的是( )

   A. 相对定位在布局中经常单独使用

   B. 相对定位一般与固定定位配合使用

   C. 项目布局中，基本不会使用相对定位

   D. 相对定位大多数使用与绝对定位配合，组成子绝父相



6. 以下选项，针对绝对定位描述错误的是( )

   A. 绝对定位元素脱离标准流

   B. 绝对定位元素实现模式转换

   C. 绝对定位元素会固定在页面某个位置, 不随着滚动条的滚动而滚动

   D. 绝对定位的元素可以使用边偏移属性



7. 固定定位元素的位移参照物是( )

   A. 自身原本的位置

   B. 参照浏览器的可视区域

   C. 参照父元素的位置

   D. 参照带有定位的元素位移



8. 下列设置中元素层级有效并且最高的是( )

   A. 

   ```css
   div { position:absolute; z-index:99 }
   ```

   B. 

   ```css
   div { position:absolute;}
   ```

   C. 

   ```css
   div { z-index:99 }
   ```

   D. 

   ```css
   div { position:absolute; z-index:2 }
   ```



9. 文字与图片之间有一个垂直对齐规则，默认是( )

   A. 中线对齐

   B. 基线对齐

   C. 顶线对齐

   D. 底线对齐



10.把一个div 变成圆形下列正确的是( )

A. 

```css
div {
width: 200px;
height: 200px;
border: 10px solid black;
border-radius: 50%;
}
```

B. 

```css
div {
width: 200px;
height: 100px;
border: 10px solid black;
border-radius: 50%;
}
```

C. 

```css
div {
width: 200px;
height: 100px;
border: 10px solid black;
border-radius: 50px;
}
```

D. 

```css
div {
width: 200px;
height: 200px;
border: 10px solid black;
border-radius: 50px;
}
```

