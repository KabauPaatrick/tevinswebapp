<template>
    <div>
      <h2>Locations & Drop-Off Points Tree</h2>
      <tree-list :model="treeData" node-key="id">
        <template v-slot="{ node, toggle, expand }">
          <div class="tree-node">
            <span @click="toggle(node)">{{ node.label }}</span>
            <button v-if="node.isLocation" @click="createChild(node)">Add Sub-Location</button>
            <button v-if="node.isLocation" @click="createDropOff(node)">Add Drop-Off</button>
            <button @click="editNode(node)">Edit</button>
            <button @click="deleteNode(node)">Delete</button>
          </div>
          <tree-list v-if="expand(node)" :model="node.children" />
        </template>
      </tree-list>
    </div>
  </template>
  
  <script>
  import { Tree } from 'vue-tree-list';  // Verify this import path and library compatibility
  
  export default {
    components: {
      'tree-list': Tree
    },
    data() {
      return {
        treeData: []
      };
    },
    created() {
      this.fetchLocationsAndDropOffs();
    },
    methods: {
      async fetchLocationsAndDropOffs() {
        try {
          const response = await fetch('https://kabau.pythonanywhere.com/api/location/locations/');
          const data = await response.json();
          this.treeData = this.transformToTreeData(data);
        } catch (error) {
          console.error('Failed to fetch locations and drop-offs:', error);
        }
      },
      transformToTreeData(data) {
        const locationMap = {};
        data.locations.forEach(location => {
          locationMap[location.id] = {
            id: location.id,
            label: location.name,
            isLocation: true,
            children: []
          };
        });
  
        const treeData = [];
        data.locations.forEach(location => {
          if (location.parent) {
            locationMap[location.parent].children.push(locationMap[location.id]);
          } else {
            treeData.push(locationMap[location.id]);
          }
  
          // Attach drop-off points to their respective locations
          location.drop_off_points.forEach(dropOff => {
            locationMap[location.id].children.push({
              id: dropOff.id,
              label: `${dropOff.name} - ${dropOff.address}`,
              isLocation: false,
              children: []
            });
          });
        });
  
        return treeData;
      },
      async createChild(node) {
        const newName = prompt('Enter the name of the new sub-location:');
        if (newName) {
          try {
            const response = await fetch('https://kabau.pythonanywhere.com/api/location/locations/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                name: newName,
                parent: node.id,
                description: ''
              })
            });
            const newLocation = await response.json();
            node.children.push({
              id: newLocation.id,
              label: newLocation.name,
              isLocation: true,
              children: []
            });
          } catch (error) {
            console.error('Failed to create sub-location:', error);
          }
        }
      },
      async createDropOff(node) {
        const newName = prompt('Enter the name of the new drop-off point:');
        const newAddress = prompt('Enter the address of the new drop-off point:');
        const newCharges = prompt('Enter the charges for the new drop-off point:');
        if (newName && newAddress && newCharges) {
          try {
            const response = await fetch('https://kabau.pythonanywhere.com/api/location/dropoffs/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                name: newName,
                address: newAddress,
                charges: parseFloat(newCharges),
                location: node.id
              })
            });
            const newDropOff = await response.json();
            node.children.push({
              id: newDropOff.id,
              label: `${newDropOff.name} - ${newDropOff.address}`,
              isLocation: false,
              children: []
            });
          } catch (error) {
            console.error('Failed to create drop-off point:', error);
          }
        }
      },
      async editNode(node) {
        if (node.isLocation) {
          const newName = prompt('Enter the new name for the location:', node.label);
          if (newName && newName !== node.label) {
            try {
              const response = await fetch(`https://kabau.pythonanywhere.com/api/location/locations/${node.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                  name: newName,
                  parent: node.parent ? node.parent.id : null,
                  description: ''
                })
              });
              const updatedLocation = await response.json();
              node.label = updatedLocation.name;
            } catch (error) {
              console.error('Failed to update location:', error);
            }
          }
        } else {
          const newName = prompt('Enter the new name for the drop-off point:', node.label.split(' - ')[0]);
          const newAddress = prompt('Enter the new address for the drop-off point:', node.label.split(' - ')[1]);
          if (newName && newAddress) {
            try {
              const response = await fetch(`https://kabau.pythonanywhere.com/api/location/dropoffs/${node.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                  name: newName,
                  address: newAddress,
                  charges: parseFloat(node.charges),
                  location: node.location
                })
              });
              const updatedDropOff = await response.json();
              node.label = `${updatedDropOff.name} - ${updatedDropOff.address}`;
            } catch (error) {
              console.error('Failed to update drop-off point:', error);
            }
          }
        }
      },
      async deleteNode(node) {
        if (confirm(`Are you sure you want to delete this ${node.isLocation ? 'location' : 'drop-off point'}?`)) {
          try {
            await fetch(`https://kabau.pythonanywhere.com/api/location/${node.isLocation ? 'locations' : 'dropoffs'}/${node.id}/`, {
              method: 'DELETE'
            });
            this.removeNode(this.treeData, node.id);
          } catch (error) {
            console.error('Failed to delete node:', error);
          }
        }
      },
      removeNode(tree, id) {
        for (let i = 0; i < tree.length; i++) {
          if (tree[i].id === id) {
            tree.splice(i, 1);
            return;
          }
          if (tree[i].children && tree[i].children.length > 0) {
            this.removeNode(tree[i].children, id);
          }
        }
      }
    }
  };
  </script>
  
  
  <style scoped>
  .tree-node {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  button {
    margin-left: 10px;
  }
  </style>
  