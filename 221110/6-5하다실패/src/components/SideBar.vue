<template>
  <div id="sidebar-box">
    <router-link to="/" class="nav-link">모든</router-link>
    <br />
    <router-link to="/today" class="nav-link">오늘</router-link>
    <br />
    <router-link to="/important" class="nav-link">중요</router-link>
  </div>
</template>

<script>
export default {
  name: "SideBar",
};
</script>

<style>

#sidebar-box {
  margin-bottom: 400px;
}
</style>
