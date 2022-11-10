import Vue from 'vue'
import Vuex from 'vuex'
import todo from '@/store/modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    CLICK_STAR(state, itemid) {
      const index = state.todo.list.findIndex((item) => {
        return item.id === itemid
      })
      state.todo.list[index].isImportant = !state.todo.list[index].isImportant
    },
    ADD_ITEM(state, item) {
      state.todo.list.push(item)
    },
    CHECKBOX_CLICK(state, itemid) {
      const index = state.todo.list.findIndex((item) => {
        return item.id === itemid
      })
      state.todo.list[index].isCompleted = !state.todo.list[index].isCompleted
    },
    UPDATE_SUBMIT(state, data) {
      const index = state.todo.list.findIndex((item) => {
        return item.id === data.id
      })
      state.todo.list[index].content = data.content
      state.todo.list[index].dueDateTime = data.date
    }
  },
  actions: {
    clickStar(context, id) {
      context.commit('CLICK_STAR', id)
    },
    addItem(context, inputvalue) {
      const date = new Date()
      const item = {
        id: new Date().getTime(),
        content: inputvalue,
        dueDateTime: new Date(+date + 3240 * 1000).toISOString().slice(0, 16) + '00:00',
        isCompleted: false,
        isImportant: false,	
      }
      context.commit('ADD_ITEM', item)
    },
    checkboxClick(context, id) {
      context.commit('CHECKBOX_CLICK', id)
    },
    addItemImportant(context, inputvalue) {
      const date = new Date()
      const item = {
        id: new Date().getTime(),
        content: inputvalue,
        dueDateTime: new Date(+date + 3240 * 1000).toISOString().slice(0, 16) + '00:00',
        isCompleted: false,
        isImportant: true,	
      }
      context.commit('ADD_ITEM', item)
    },
  },
  modules: {
    todo,
  }
})
