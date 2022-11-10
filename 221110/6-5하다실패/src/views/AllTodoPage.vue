<template>
  <div class="alltodo-box">
    <h1>모든 할일</h1>
    <div class="plus-item">
      <label class="plus-label">+</label>
      <input @keyup.enter="addItem" v-model="inputvalue" type="text" class="plus-todo" placeholder="할 일을 작성해주세요!">
    </div>
    <hr>
    <div v-for="todo in todolist" :key="todo.id">
      <div class="todo-box" @click="openUpdateForm">
        <input type="checkbox" class="checkbox" v-if="todo.isCompleted" checked @click="checkboxClick(todo.id)">
        <input type="checkbox" class="checkbox" v-else unchecked @click="checkboxClick(todo.id)">
        <label class="checkbox-label">{{ todo.content }}</label>
        <div class="star-icon">
          <button @click="clickstar(event)" class="bi" :class="{ 'bi-star-fill': todo.isImportant , 'bi-star': !todo.isImportant}"></button>
        </div>
      </div>
      <div class="updateform displayNone" display>
        <button @click="updatesubmit(todo.id)" class="updatebutton">수정하기</button>
        <br>
        <input class="contentinput" type="text" :value=todo.content><br>
        <input class="dateinput" type="text" :value="todo.dueDateTime">
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "AllTodoPage",
  data() {
    return {
      todolist: this.$store.state.todo.list,
      inputvalue: null,
    };
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
    },
    openUpdateForm(event) {
      event.target.nextSibling.classList.toggle('displayNone')
    },
    updatesubmit(id) {
      console.log(id)
    }
  }
};
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
.displayNone {
  display: none;
}
.updatebutton {
  background-color: green;
  border-radius: 5px;
  margin-bottom: 5px;
  color: white;
}
.updateform {
  height: 80px;
  background-color: rgb(187, 255, 255);
  margin-bottom: 20px;
  border-radius: 10px;
  padding: 10px;
  width: 98%;
  box-shadow: 1px 2px 2px gray;
  padding-bottom: 10px;
}
.contentinput {
  height: 20px;
  padding: 0px;
  width: 100%;
  margin-bottom: 5px;
}
.dateinput {
  height: 20px;
  padding: 0px;
  width: 100%;
}
</style>
