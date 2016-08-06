# Script params
path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# Make sure using right virtualenv
correct_python=$path/jujika_env/bin/python
python_path=`which python`

if [ $python_path != $correct_python ];
then
    echo "Incorrect virtual environment: $python_path"
    exit 1
fi

# Install requirements
requirements_file=$path/requirements.txt
requirements_lock_file=$path/requirements.lock

if [ -f $requirements_file ];
then
   echo "Loading requirements from: $requirements_file"
   pip install -r $requirements_file 
   pip freeze > $requirements_lock_file
else
   echo "Error requirements file does not exist: $requirements_file"
fi
