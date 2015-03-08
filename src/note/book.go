package note

import (
	"gopkg.in/mgo.v2/bson"
	"time"
)

type Book struct {
	Id bson.ObjectId `bson:"_id,omitempty" table:"book"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 作者
	Author string `bson:"author,omitempty" json:"author"`
	//简介
	Summary string `bson:"summary,omitempty" json:"summary"`
	// 注释数量
	Size rune `bson:"size,omitempty" json:"size"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 修改时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
}
