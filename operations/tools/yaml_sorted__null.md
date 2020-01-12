## yaml 按顺序 load,dump
当你有一个 map.里面有dict,list各种的时候， 如果你用 yaml.load,yaml.dump,你会发现他的顺序有变了， 当你不洗碗他变的时候， 怎么办？？
```
from collections import OrderedDict
import yaml

def ordered_yaml_load(yaml_path, Loader=yaml.Loader,
                      object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    with open(yaml_path) as stream:
        return yaml.load(stream, OrderedLoader)


def ordered_yaml_dump(data, filename, Dumper=yaml.SafeDumper):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())
            
    ## 这里是 把 生成文件里的 “null” 转为 “”
    def represent_none(self,_):        
     	return self.represent_scalar('tag:yaml.org,2002:null','')

    stream = None
    with open(filename, "w") as stream:
        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        OrderedDumper.add_representer(type(None), represent_none)
        yaml.dump(data,
                  stream,
                  OrderedDumper,
                  default_flow_style=False,
                  encoding='utf-8',
                  allow_unicode=True)
 
 
 ###  使用 
kv_conf_tmpl = ordered_yaml_load("./kkkk.conf")
ordered_yaml_dump(kv_conf_tmpl, "./after_kk.conf")

```
## yaml.dump 有个坑， 当你文件是none，它会打印出“null”
这就很烦了。所以，需要去掉。  （上面的例子里也有介绍）
```
def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(type(None), represent_none)

```

参考链接(https://stackoverflow.com/questions/37200150/can-i-dump-blank-instead-of-null-in-yaml-pyyaml?answertab=active#tab-top)
