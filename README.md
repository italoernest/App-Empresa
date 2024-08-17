<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business and Supplier Management System</title>
</head>
<body>
    <h1>Project Overview: Business and Supplier Management System</h1>

    <h2>Introduction</h2>
    <p>
        This project is a <strong>Business and Supplier Management System</strong> developed using 
        <strong>Django</strong> and <strong>Python</strong>. The system allows you to manage business entities, 
        suppliers, and their related data such as addresses, CNPJ (Brazilian company identification number), contact 
        information, and more. It provides features to create, read, update, and delete (CRUD) these entities while 
        ensuring data validation and security.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Business Management:</strong> Create and manage businesses, including attributes like CNPJ, Inscrição 
        Estadual (State Registration), phone numbers, WhatsApp contact, and address information.</li>
        <li><strong>Supplier Management:</strong> Manage suppliers with similar features as the business management module.</li>
        <li><strong>Data Validation:</strong> Ensures valid CNPJ format, phone number formats, and other fields using custom 
        validators and the <code>validate-docbr</code> package.</li>
        <li><strong>Timestamps:</strong> Automatic tracking of creation and update times for each business and supplier.</li>
        <li><strong>UUID for Primary Keys:</strong> Uses UUID for the primary key in both the <code>Business</code> and 
        <code>Supplier</code> models, ensuring secure and unique identifiers.</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Python:</strong> Core programming language.</li>
        <li><strong>Django:</strong> Web framework used to build the project.</li>
        <li><strong>PostgreSQL/MySQL:</strong> (Optional) Database backend, though SQLite is sufficient for local development.</li>
        <li><strong>Crispy Forms:</strong> For rendering responsive, user-friendly forms.</li>
        <li><strong>JQuery Mask Plugin:</strong> For adding input masks to fields like CNPJ and phone numbers.</li>
        <li><strong>validate-docbr:</strong> A package used for CNPJ validation in Brazil.</li>
    </ul>

    <h2>Models</h2>
    <h3>Business</h3>
    <ul>
        <li><code>id</code> (UUID)</li>
        <li><code>nome_empresa</code> (Company Name)</li>
        <li><code>cnpj</code> (Validated CNPJ)</li>
        <li><code>inscricao_estadual</code> (State Registration)</li>
        <li><code>telefone</code>, <code>whatsapp</code> (Validated contact fields)</li>
        <li><code>logradouro</code>, <code>numero</code>, <code>complemento</code>, <code>bairro</code>, <code>cidade</code>, 
        <code>estado</code>, <code>cep</code> (Address details)</li>
        <li><code>observacao</code> (Notes)</li>
        <li><code>created_at</code>, <code>updated_at</code> (Timestamps)</li>
    </ul>

    <h3>Supplier</h3>
    <p>Similar structure as <code>Business</code> but focused on supplier data.</p>

    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li><strong>Python 3.x</strong></li>
        <li><strong>Django 4.x</strong></li>
        <li><strong>Virtualenv</strong> (optional but recommended)</li>
        <li><strong>PostgreSQL or MySQL</strong> (optional for production)</li>
    </ul>

    <h3>Steps</h3>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/yourusername/business-supplier-management.git
cd business-supplier-management</code></pre>
        </li>
        <li><strong>Create a Virtual Environment:</strong>
            <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run Migrations:</strong>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li><strong>Run the Development Server:</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the Application:</strong>
            <p>Open your browser and go to <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>.</p>
        </li>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li><strong>Admin Dashboard:</strong> Use the Django admin interface to create, update, and delete businesses and 
        suppliers. Access it via <a href="http://127.0.0.1:8000/admin/" target="_blank">http://127.0.0.1:8000/admin/</a>.</li>
        <li><strong>Custom Views:</strong> Custom views for managing businesses and suppliers via web forms are available 
        at their respective URLs.</li>
    </ul>

    <h2>Configuration</h2>
    <h3>Database</h3>
    <p>You can change the database settings in the <code>settings.py</code> file to use PostgreSQL, MySQL, or any other 
    supported database.</p>

    <h3>Static Files</h3>
    <p>Ensure you run the following command to collect static files when deploying to production:</p>
    <pre><code>python manage.py collectstatic</code></pre>

    <h2>Testing</h2>
    <p>To run the test suite:</p>
    <pre><code>python manage.py test</code></pre>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contributing</h2>
    <p>Feel free to submit a pull request or open an issue if you find any bugs or have feature requests. Contributions are welcome!</p>
</body>
</html>
