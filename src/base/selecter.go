package base

// 选择器
type Selecter struct {
	Id    string `json:"id"`
	Title string `json:"title"`
}

// 根据map创建选择器列表
func Selecter4Map(m map[string]string) (s []Selecter) {
	for k, v := range m {
		s = append(s, Selecter{
			Id:    k,
			Title: v,
		})
	}
	return
}
