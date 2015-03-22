package base

import (
	"reflect"
	"strings"
)

// 删除Slice元素
func SliceRemove(slice, element interface{}) {
	sv := reflect.ValueOf(slice).Elem()
	for i := 0; i < sv.Len(); i++ {
		if reflect.DeepEqual(sv.Index(i).Interface(), element) {
			before := sv.Slice(0, i)
			after := sv.Slice(i+1, sv.Len())
			reflect.Copy(sv, reflect.AppendSlice(before, after))
			sv.SetLen(sv.Len() - 1)
			return
		}
	}
}

// 字符串分割
func SplitAfter(s string, sep []string) []string {
	c := 0
	for _, sp := range sep {
		c += strings.Count(s, sp)
	}
	ret := []string{s}
	if c == 0 {
		return ret
	}
	for _, sp := range sep {
		n := []string{}
		for _, r := range ret {
			for _, a := range strings.SplitAfter(r, sp) {
				aa := strings.TrimSpace(a)
				if aa != "" {
					n = append(n, aa)
				}
			}
		}
		ret = n
	}
	return ret
}
