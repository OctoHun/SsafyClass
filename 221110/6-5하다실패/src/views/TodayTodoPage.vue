<template>
  <div class="alltodo-box">
    <h1>오늘 할일</h1>
    <div class="plus-item">
      <label class="plus-label">+</label>
      <input @keyup.enter="addItem" v-model="inputvalue" type="text" class="plus-todo" placeholder="할 일을 작성해주세요!">
    </div>
    <hr>
    <div v-for="todo in Todaylist" :key="todo.id" class="todo-box">
      <input type="checkbox" class="checkbox" v-if="todo.isCompleted" checked @click="checkboxClick(todo.id)">
      <input type="checkbox" class="checkbox" v-else unchecked @click="checkboxClick(todo.id)">
      <label class="checkbox-label">{{ todo.content }}</label>
      <div class="star-icon">
        <button @click="clickstar(todo.id)" class="bi" :class="{ 'bi-star-fill': todo.isImportant , 'bi-star': !todo.isImportant}"></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'TodayTodoPage',
    data() {
      return {
        todolist: this.$store.state.todo.list,
        inputvalue: null
      }
    },
    computed: {
      Todaylist() {
        const date = new Date()
        const list = this.todolist.filter((item) => {
          return (item.dueDateTime.slice(0, 10) === new Date(+date + 3240 * 1000).toISOString().slice(0, 10) && item.isCompleted === false)
        })
        return list
      }
    },
    methods: {
      clickstar(id) {
        this.$store.dispatch('clickStar', id)
      },
      addItem() {
        this.$store.dispatch('addItem', this.inputvalue)
        this.inputvalue = null
      },
      checkboxClick(id) {
      this.$store.dispatch('checkboxClick', id)
    }
    },
}
</script>

<style>
.checkbox{
  margin-left: 10px;
}
.checkbox-label{
  margin-left: 10px;
}
.todo-box{
  display: flex;
  align-items: center;
  width: 100%;
  height: 80px;
  box-shadow: 1px 2px 2px gray;
  margin-bottom: 20px;
  border-radius: 10px;
  padding-right: 10px;
}
.alltodo-box {
  padding-right: 20px;
}
.star-icon{
  margin-left: auto;
}
.bi {
  color: rgb(255, 239, 9);
  border: 0px;
  background-color: white;
}
.plus-item{
  display: flex;
}
.plus-label{
  font-size: 30px;
  margin-right: 10px;
}
.plus-todo {
  height: 40px;
  width: 100%;
}
</style>