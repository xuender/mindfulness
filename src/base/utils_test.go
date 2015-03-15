package base

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

func TestSliceRemove(t *testing.T) {
	Convey("数组删除 SliceRemove", t, func() {
		s := []string{"1", "2", "4", "5"}
		Convey("删除成功", func() {
			SliceRemove(&s, "4")
			So(len(s), ShouldEqual, 3)
			So(s[2], ShouldEqual, "5")
			SliceRemove(&s, "1")
			So(len(s), ShouldEqual, 2)
			So(s[1], ShouldEqual, "5")
			SliceRemove(&s, "5")
			So(len(s), ShouldEqual, 1)
			So(s[0], ShouldEqual, "2")
		})
		Convey("删除异常", func() {
			SliceRemove(&s, "533")
			So(len(s), ShouldEqual, 4)
			So(s[3], ShouldEqual, "5")
		})
	})
}
func TestSplitAfter(t *testing.T) {
  Convey("字符串分割 SpliteAfter", t, func() {
    Convey("12345 2,4", func() {
      ret := SplitAfter("12345", []string{"2", "4"})
      So(len(ret), ShouldEqual, 3)
      So(ret[0], ShouldEqual, "12")
      So(ret[1], ShouldEqual, "34")
      So(ret[2], ShouldEqual, "5")
    })
    Convey("12345 2,3", func() {
      ret := SplitAfter("12345", []string{"2", "3"})
      So(len(ret), ShouldEqual, 3)
      So(ret[0], ShouldEqual, "12")
      So(ret[1], ShouldEqual, "3")
      So(ret[2], ShouldEqual, "45")
    })
    Convey("12345 2,5", func() {
      ret := SplitAfter("12345", []string{"2", "5"})
      So(len(ret), ShouldEqual, 2)
      So(ret[0], ShouldEqual, "12")
      So(ret[1], ShouldEqual, "345")
    })
  })
}
