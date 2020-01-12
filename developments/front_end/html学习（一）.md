插入多个空格时，请输入`&nbsp;`或`&#160;`
   `&ensp; ` — “en空格”是根据字体排印学的计量单位命名，宽度是两个普通空格的宽度
   `&emsp;`  — “em空格”大概是四个普通空格的宽度
创建换行符`<br>`
使用预格式化的文本。“pre”元素可以定义预格式化的文本，会保留文本里的空格或换行符。因此，在`<pre></pre>`
用“p”标签定义段落。p 元素会自动在其前后创建一些空白，因此，文本后的 `<p></p>`
<ｈｒ> 标签在 HTML 页面中创建一条水平线。`<hr>`

####在html中用ｆｏｒ，　ｉｆ.
```
                        {%if endpoint_all_problem_metric[key]%}   
                            {%for metric in endpoint_all_problem_metric[key]%}
                                {{metric}}&nbsp;
                            {%endfor%} 
                        {%endif%}
```
####在html中输出  [  ，¦ ，]  ， href超链接。
```
                    <span class="gray">[</span>
                    <span class="endpoint">{{endpoint_all_page[key][0].endpoint}}</span> 
                    <span class="cut-line">¦</span>
                    <span class="orange">{{endpoint_all_page[key][0].timestamp|time_duration}}</span>
                    <span class="cut-line">¦</span>
                    <a href="/portal/alarm-dash/case_point2?case_endpoint={{endpoint_all_page[key][0].endpoint}}">{{_('event list')}}</a>
                    <span class="gray">]</span>
                    </br>
                    <hr>
```
#### button使用portal.js

```
 <button class="btn btn-warning btn-sm" onclick="alarm_endpoint_batch_rm();">{{_('batch delete')}}</button>
```
#### 继承
{% extends "portal/layout.html" %}　　继承某某
{% block content %}
{%endblock%}　　　这两个中间就是可以修改的内容.

```
{% extends "base.html" %}


{%block navbar%}
  {%include "navbar.html"%}
{%endblock%}

```
### scripts

```

<h1 onclick="alert('点击了H1');console.log('控制台显示')">点击</h1>　　<!-- onclick 点击。-->
<script src="index.js">
	alert("资源引入时的标签内容");		// alert 弹出一个　提示信息
	prompt('请输入出生年份');    		// prompt 弹出了一个 填空。
	confirm("提示文本")				//确认框
	document.write('文档写入'); 		 // document.write 写在了 网页上
	
	if(score >= 90){
			console.log("A");
		}else if (score >= 80)
		{
			console.log("B");
		}else if (score >= 60)
		{
			console.log("C");
		}else {
			console.log("D");
		}

	switch(input){						// 匹配
			case '5':
				console.log("周五");
			case '6':
				console.log("周六");
				break;
			default :
				console.log("请输入合法的值");		//默认
		}

		var i = 1;
		var sum = 0;
		while(i <= 100){ 				//while 
			//console.log(i);
			sum += i;
			i ++;
		}
		do{							// do   while
			console.log(i);
			i ++;
		}while(i < 101);
		do{
			input = prompt("请输入数据,exit表示退出");
		}while(input != "exit");

		var res = age > 28 ? "人到中年不得已" : "还年轻,继续浪";        		// 三目 表达式。
		for(var i = 1;i < 101;i ++){							// for循环。
			//console.log(i);
		}


		var isRun = year % 4 == 0 && year % 100 != 0 || year % 400 == 0;
		var i = 1;
		//通过循环控制当前月之前所有整月天数累加
		while(i < month){ //i 取 1 ~ month-1
			switch(i){
				case 1 :
				case 3 :
				case 5 :
				case 7 :
				case 8 :
				case 10:
					sum += 31;
					break;
				case 4:
				case 6:
				case 9:
				case 11:
					sum += 30;
					break;
				case 2:
					sum += 28;
					if(isRun)
					sum += 1;
					break;			
			}
			i ++;
		}
		
		
</script>


```

```
			function 函数名(参数列表){
				函数体;
				return 返回值;
			}
		function f2(){				//局部变量
			console.log(arguments.callee)  		 // function f2() // 指向当前执行的函数
			console.log(arguments.length)    	//1		//指向传递给当前函数的参数数量
			console.log(arguments[0])			//1000   // 第一个元素
			console.log(arguments[1])			//undefined 	// 第二个元素 
			console.log(arguments);
		}
		f2(1000);


		//1. 匿名函数
		var fn = function (){}; 
		定义变量保存函数地址,等同于函数名
		 调用 :
			fn();
			
		//2. 匿名函数自执行
		(function (a) {
			console.log(a);
		})(100);
```

```
Array String RegExp Math Date...
					1. 字面量方式
							var arr1 = [10,'20',true];
					2. new 关键字创建
							//创建的同时初始化元素
							var arr2 = new Array(10,20,30);
							//只传入一个number值,表示指定数组长度
							var arr3 = new Array(5);
					arr.length;
				for(var i = 0; i < arr.length; i ++){
					console.log(arr[i]);
				}

				for(var j = arr.length-1; j >= 0; j --){
					console.log(arr[j]);
				}
				
	var arr1 = [10,20,30];
	//2. for - in 快速for循环
	for(var key in arr1){
		//获取数组元素下标
		console.log(key);
	}
	//3. forEach() 方法可以遍历数组获取元素 和 下标。
	arr1.forEach(function (element,index){
		console.log(element,index);
	});
0
1 
2 
10 0 
20 1 
30 2
```

