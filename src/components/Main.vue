<template>
  <div class="main">
    <h1>Welcome To My Simple To Do List</h1>
    <div v-show="!displayCat">
      <button @click="toggleDisplayCat">Show By Category</button>
      <div v-for="task in lot" :class="{complete: task.complete, incomplete: !task.complete}">
        <h2>{{ task.title }}</h2>
        <li>
          Due Date: {{ task.due }}
        </li>git
        <li>
          Category: {{ task.category }}
        </li>
        <li>
          Description: {{ task.desc }}
        </li>
        <button @click="removeTask(task.id)">Delete Task</button>
        <button v-show="!task.complete" @click="toggleTaskCompletion(task)">Mark as Complete</button>
        <button v-show="task.complete" @click="toggleTaskCompletion(task)">Mark as Incomplete</button>
      </div>
    </div>
    <div>
      <div v-show="displayCat">
        <button @click="toggleDisplayCat">Show All</button>
        <p>Search Category:</p>
        <p><input type="text" v-model="selectedCat"></p>
        <div v-for="task in filterCategory(selectedCat)" :class="{complete: task.complete, incomplete: !task.complete}">
          <h2>{{ task.title }}</h2>
          <li>
            Due Date: {{ task.due }}
          </li>
          <li>
            Category: {{ task.category }}
          </li>
          <li>
            Description: {{ task.desc }}
          </li>
          <button @click="removeTask(task.id)">Delete Task</button>
        </div> 
      </div>
    </div>
    <div>
      <h2>Add New Task</h2>
      <p>Enter Task Title</p>
      <input type="text" v-model="title">
      <p>Enter Task Category</p>
      <input type="text" v-model="category">
      <p>Enter Task Due Date</p>
      <input type="datetime-local" v-model="due">
      <p>Enter Task Description</p>
      <textarea v-model="desc" cols="100" rows="10"></textarea>
      <p><button @click="addTask">Add Task</button></p>
    </div>
  </div>
</template>
  
<script>
  export default {
    data() {
      return {
        displayCat: false,
        selectedCat: '',
        idCounter: 0,
        lot: [{id: 0, title: "Task Title", desc: "Example Description", due: "Due Date", category: "Task Category", complete: false}],
        task: '',
        title: '',
        desc: '',
        due: '',
        category: '',
      };
    },
    methods: {
      addTask() {
        this.idCounter++;
        this.lot.push({id: this.idCounter, title: this.title, desc: this.desc, due: this.due, category: this.category, complete: false});
      },
      filterCategory() {
        return this.lot.filter((t) => (t.category.startsWith(this.selectedCat)));
      },
      removeTask(id) {
        this.lot = this.lot.filter((t) => t.id != id);
      },
      toggleDisplayCat() {
        this.displayCat = !this.displayCat;
      },
      toggleTaskCompletion(task) {
        task.complete = !task.complete;
      }
    }
  };
  </script>
  
  <style scoped>
  .main {
    display: block;
    justify-content: left;
  }
  h1 {
    color: #42b983;
  }
  .complete {
    background-color: lightgreen;
  }
  .incomplete {
    background-color: lightcoral;
  }
  </style>
  