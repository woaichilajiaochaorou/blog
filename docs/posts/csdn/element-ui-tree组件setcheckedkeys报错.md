---
title: "element ui tree组件setCheckedKeys报错"
date: 2023-02-15
description: "element ui tree组件报错"
tags:
  - CSDN迁移
---

# element ui tree组件setCheckedKeys报错

### Error in nextTick: “TypeError: Cannot read properties of undefined (reading ‘setCheckedKeys’)”

> **记得把nextTick方法放在this.permsDialogVisible = true的后面**
    
    
                //打开分配权限对话框
                allocatePerms(row) {
                    //获取当前打开的用户所拥有的权限树
                    this.$http.get(`menu/checkedTree/${row.roleId}`).then(res => {
                        if (res.data.code !== 1) {
                            return this.$message.error('获取用户权限树失败')
                        }
    
                        this.permsDialogVisible = true
                        this.$nextTick(()=>{
                            this.$refs.permissionTree.setCheckedKeys(res.data.data)
                        })
                           
                    })
                
                },
