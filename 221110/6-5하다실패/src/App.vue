<template>
  <div id="app">
    <nav id="nav-box">
      <SideBar/>
    </nav>
    <article id="article-box">
      <router-view/>
    </article>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'

export default {
    name: 'TodayTodoPage',
    components: {
      SideBar,
    }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: flex;
  padding-left: 20px;
  padding-right: 20px;
}

nav {
  text-align: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav-box {
  border: 1px solid black;
  border-radius: 10px;
  margin-right: 10px;
  width: 20%;
  padding-top: 20px;
}

#article-box {
  border: 1px solid black;
  border-radius: 10px;
  width: 100%;
  padding: 20px;

}
.nav-link {
  text-decoration: none;
  font-size: 25px;
}
nav a.router-link-exact-active {
  color: #42b983;
}



</style>