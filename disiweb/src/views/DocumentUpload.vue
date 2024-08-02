<template>
    <div class="container mt-5">
        <!-- Document Form -->
        <div class="card mb-4">
            <div class="card-header">
                <h2 class="mb-0">Upload a Document</h2>
            </div>
            <div class="card-body">
                <form @submit.prevent="submitDocument">
                    <!-- Folder ID -->
                    <div class="form-group">
                        <label for="folderId">Folder ID</label>
                        <input type="text" class="form-control" id="folderId" v-model="document.folder_id" placeholder="Enter folder ID" required>
                    </div>
                    <!-- Document Name -->
                    <div class="form-group">
                        <label for="documentName">Document Name</label>
                        <input type="text" class="form-control" id="documentName" v-model="document.document_name" placeholder="Enter document name" required>
                    </div>
                    <!-- Version Name -->
                    <div class="form-group">
                        <label for="versionName">Version Name</label>
                        <input type="text" class="form-control" id="versionName" v-model="document.version_name" placeholder="Enter version name" required>
                    </div>
                    <!-- File Upload -->
                    <div class="form-group">
                        <label for="documentFile">Select Document</label>
                        <input type="file" class="form-control-file" id="documentFile" @change="handleFileUpload" required>
                    </div>
                    <!-- Submit Button -->
                    <div class="row mt-3">
                        <div class="col-md-6">
                            <button type="submit" class="btn btn-primary">Upload</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    setup() {
        const document = {
            folder_id: '',
            document_name: '',
            version_name: '',
            document: null,
            token: localStorage.getItem('edms_token') || '' // Retrieve token from localStorage
        };

        const submitDocument = async () => {
            try {
                // Validate document
                if (!document.document) {
                    throw new Error('Please select a document file.');
                }

                const formData = new FormData();
                formData.append('folder_id', document.folder_id);
                formData.append('document_name', document.document_name);
                formData.append('version_name', document.version_name);
                formData.append('document', document.document); // Append the file object directly

                const config = {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': `Bearer ${document.token}` // Include the authorization token
                    }
                };

                const response = await axios.post('https://kabau.pythonanywhere.com/api/folder/documents/upload', formData, config);
                console.log(response.data);
                // Clear form fields after successful submission
                document.folder_id = '';
                document.document_name = '';
                document.version_name = '';
                document.document = null;
            } catch (error) {
                console.error('Error submitting document:', error.message);
            }
        };

        const handleFileUpload = (event) => {
            document.document = event.target.files[0];
        };

        return {
            document,
            submitDocument,
            handleFileUpload
        };
    }
};
</script>
