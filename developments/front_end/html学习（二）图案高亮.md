目的： 在open-falcon-dashboard的 alarm-dashboard 上,增加一个Alarm-Dashboard-V2.
为了让他显示高亮。 

1    首先定位到 代码位置。 /open-falcon-dashboard/rrd/templates/navbar.html
就照着原来的 模仿了下.
```
          <li {%if g.nav_menu == "p_nodata"%}class="active"{%endif%}><a href="/portal/nodata">Nodata</a></li>
          <li {%if g.nav_menu == "p_alarm-dash"%}class="active"{%endif%}><a href="/portal/alarm-dash/case">Alarm-Dashboard</a></li>
          <li {%if g.nav_menu == "p_alarm-dash-V2"%}class="active"{%endif%}><a href="/portal/alarm-dash-V2/case_point">Alarm-Dashboard-V2</a></li>
```
首先注意到： if g.nav_menu == "p_alarm-dash-V2"：class="active".
直觉pandan是否高亮， active是动作，   g.nav_meuv是判断条件。 

2接着再次寻找。 g.nav_meuv

```
root@dddd:/open-falcon-dashboard# grep -ilr p_alarm-dash
rrd/view/.__init__.py.swp
rrd/view/__init__.py
rrd/templates/navbar.html
```
查看`rrd/view/__init__.py`

```

@app.before_request
def app_before():
    g.user_token = get_usertoken_from_session(session)
    g.user = get_current_user_profile(g.user_token)
    g.locale = request.accept_languages.best_match(config.LANGUAGES.keys())

    path = request.path
    if not g.user and not path.startswith("/auth/login") and \
            not path.startswith("/static/") and \
            not path.startswith("/portal/links/") and \
            not path.startswith("/auth/register"):
        return redirect("/auth/login")

    if path.startswith("/screen"):
        g.nav_menu = "nav_screen"
    elif path.startswith("/portal/hostgroup") or path.startswith("/portal/group"):
        g.nav_menu = "p_hostgroup"
    elif path.startswith("/portal/template"):
        g.nav_menu = "p_template"
    elif path.startswith("/portal/expression"):
        g.nav_menu = "p_expression"
    elif path.startswith("/portal/nodata"):
        g.nav_menu = "p_nodata"
    elif path.startswith("/portal/alarm-dash"):
        g.nav_menu = "p_alarm-dash"
    else:
        g.nav_menu = ""
```
于是又模仿写了下

```
  elif path.startswith("/portal/alarm-dash-V2"):
        g.nav_menu = "p_alarm-dash-V2"
```
发现不对劲。 alarm-dash一直都在高亮（当点击alarm-dash-V2）。
于是研究了下， flask的g。  startwith ，endwith。
最后。重新改下了下。 

```
    elif path.endswith("/portal/alarm-dash/case"):
        g.nav_menu = "p_alarm-dash"
    elif path.endswith("/portal/alarm-dash-V2/case_point"):
        g.nav_menu = "p_alarm-dash-V2"
```
成功。
###############################################################################
startwith: endwith; 做文本处理的时候经常要判断一个文本有没有以一个子串开始，或者结束。Python为此提供了两个函数：
S.startswith(prefix[, start[, end]]) -> bool

```
做个实例：
>>> “fish”.startswith(”fi”)
True
>>> “fish”.startswith(”fi”,1)
False
>>> “fish”.endswith(”sh”)
True
>>> “fish”.endswith(”sh”,3)
False
```
################################################################################3

size="15" style="width:451px; height:20px;"  用来控制 input 对话框 的长度的, 
autocomplete="on"  自动将历史信息记录 . 
```
<input type="text" size="15" style="width:451px; height:20px;" value='' autocomplete="on" />
```


