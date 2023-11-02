
## 上传方法
1. python setup.py sdist build
2. twine upload dist/*


## 主要功能
- 基本文件操作
  - `json`文件读写 

>  load_json 读取json文件  
>  write_json 写入json文件


## 使用方法
```
pip install yantu_python_util
```

```python
from yantu_python_utils.operate_json import write_json,load_json

write_json(data="your json data",filepath="your file path")
load_json(filepath="your file path")
```

