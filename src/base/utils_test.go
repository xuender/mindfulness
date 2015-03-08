package base

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

func TestSliceRemove(t *testing.T) {
	Convey("Slice Remove", t, func() {
		s := []string{"1", "2", "4", "5"}
		Convey("remove", func() {
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
		Convey("remove error", func() {
			SliceRemove(&s, "533")
			So(len(s), ShouldEqual, 4)
			So(s[3], ShouldEqual, "5")
		})
	})
}
